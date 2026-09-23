# Handwritten Cyrillic OCR trial, 2026-09-23

The source is `sources/raw/manuscript-full-91-146/142.pdf` (SHA-256
`2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f`).
PDF page 101 was rendered to PNG. Three overlapping crops from its opening
lines were passed to the MIT-licensed
`cyrillic-trocr/trocr-handwritten-cyrillic` model using Transformers 4.48.3
and CPU PyTorch 2.5.1. The model card describes training for Russian,
Ukrainian, and Church Slavonic handwriting; Kyrgyz is outside its stated
target. The software environment and model remain in ignored local `tmp/`
and the Hugging Face cache.

| crop | model output | visual/printed comparison |
| --- | --- | --- |
| first | `Из роже сактатану,` | Opening manuscript wording appears to correspond to printed `Көлөкө жерге сактаткан,` (`seytek-2012:p0974:b003:l007`), but the crop cuts into neighboring handwriting. |
| second | `былоко вин каптатком,` | Approximate letter pattern of `Пил терисин каптаткан.` in the printed witness; not a correct reading. |
| third | `Изы Рехі́лище въ колесниц и҆` | Unusable hallucinated Church Slavonic-like wording. |

The model may help search for approximate printed counterparts, but this
three-crop trial does **not** validate any manuscript baseline or yield new
translated lines. A full-page or line-level transcription still requires
direct image checking. Do not use this OCR output as Kyrgyz source text or
English translation.

## Whole-region follow-up: Rukopys-OCR-4B

The Apache-2.0 `ebinan92/Rukopys-OCR-4B` model is trained for Ukrainian
handwritten documents and publishes region-level JSON output. Its quantized
GGUF conversion was run locally with llama.cpp 0.4.1 against the upper half
of manuscript PDF page 101. The trial kept the model card's Ukrainian prompt.
It detected roughly the line layout, but the text remained substantially
wrong: the first two readings were `Колоко жоре сахтатком,` and
`на трельник каптат как,` where the directly checked printed counterparts
are `Көлөкө жерге сактаткан,` and `Пил терисин каптаткан.` Later rows
devolved into Russian/Ukrainian-like nonwords, and the 1,500-token output
limit cut off the JSON. The output is **not** a reliable Kyrgyz transcription.

Model sources: <https://huggingface.co/ebinan92/Rukopys-OCR-4B> and the
quantized conversion <https://huggingface.co/Axway/Rukopys-OCR-4B-GGUF>.
The experimental model weights and output remain ignored local scratch in
`tmp/rukopys-ocr/`; no source or release row uses them.
