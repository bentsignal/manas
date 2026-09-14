export const WINDOW_SIZE = 2048;
export function windowFor(index, total) {
  if (!Number.isInteger(index) || !Number.isInteger(total) || total < 1 || index < 0 || index >= total) throw new RangeError('Invalid line position');
  const start = Math.max(0, Math.min(index - 512, total - WINDOW_SIZE));
  return { start, count: Math.min(WINDOW_SIZE, total - start) };
}
export function chunkFor(index, chunkSize = 256) { return Math.floor(index / chunkSize); }
export function parseLine(hash, total) {
  const m = /^#line-(\d+)$/.exec(hash);
  const n = m ? Number(m[1]) : NaN;
  return Number.isSafeInteger(n) && n >= 1 && n <= total ? n - 1 : null;
}
