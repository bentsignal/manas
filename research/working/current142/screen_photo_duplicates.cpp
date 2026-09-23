// Candidate screen only: confirm any match against the original PDF images.
// Input directory holds grayscale PNG thumbnails named page-000.png for PDF 1,
// page-001.png for PDF 2, and so on. Requires OpenCV 4.
#include <opencv2/opencv.hpp>
#include <opencv2/features2d.hpp>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char **argv) {
  if (argc != 4) {
    std::cerr << "usage: screen_photo_duplicates THUMB_DIRECTORY FIRST_PDF_PAGE LAST_PDF_PAGE\n";
    return 2;
  }
  const std::string directory = argv[1];
  const int first = std::stoi(argv[2]);
  const int last = std::stoi(argv[3]);
  if (first < 1 || last < first) return 2;
  std::vector<std::vector<cv::KeyPoint>> keypoints(last + 1);
  std::vector<cv::Mat> descriptors(last + 1);
  auto detector = cv::SIFT::create(900);
  for (int page = first; page <= last; ++page) {
    char name[32];
    std::snprintf(name, sizeof(name), "/page-%03d.png", page - 1);
    cv::Mat image = cv::imread(directory + name, cv::IMREAD_GRAYSCALE);
    if (image.empty()) {
      std::cerr << "missing thumbnail for PDF page " << page << "\n";
      return 1;
    }
    detector->detectAndCompute(image, cv::noArray(), keypoints[page],
                               descriptors[page]);
  }
  cv::BFMatcher matcher(cv::NORM_L2);
  std::cout << "page_a\tpage_b\tratio_matches\transform_inliers\n";
  for (int a = first; a <= last; ++a) {
    for (int b = a + 1; b <= last; ++b) {
      if (descriptors[a].empty() || descriptors[b].empty()) continue;
      std::vector<std::vector<cv::DMatch>> candidates;
      matcher.knnMatch(descriptors[a], descriptors[b], candidates, 2);
      std::vector<cv::Point2f> points_a, points_b;
      for (const auto &pair : candidates) {
        if (pair.size() < 2 || pair[0].distance >= 0.72f * pair[1].distance)
          continue;
        points_a.push_back(keypoints[a][pair[0].queryIdx].pt);
        points_b.push_back(keypoints[b][pair[0].trainIdx].pt);
      }
      int inliers = 0;
      if (points_a.size() >= 8) {
        cv::Mat mask;
        cv::findHomography(points_a, points_b, cv::RANSAC, 4.0, mask);
        if (!mask.empty()) inliers = cv::countNonZero(mask);
      }
      if (inliers >= 8 || points_a.size() >= 15)
        std::cout << a << '\t' << b << '\t' << points_a.size() << '\t'
                  << inliers << '\n';
    }
  }
}
