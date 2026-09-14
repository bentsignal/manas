# Page 48 PDF content-stream inspection

PyMuPDF 1.27.2.3 inspected the base PDF page48 on 14 September2026 UTC. It has no images. At baseline y88.320 the text trace contains only visible black, opaque Calibri glyphs for `Т/*`, spaces, `о`, spaces, `и`, spaces. No additional hidden/invisible characters appeared in that region. The decoded content stream is preserved locally at tmp/page48-content-stream.txt. This inspection did not recover any missing wording; it supports retaining the explicit damaged-source region. It does not establish how many original verses were lost.

The live reader now displays a plain editorial marker at the exact source position. The marker is stored separately from translation rows, excluded from translated-line and English-word totals, and prevents completeness certification.
