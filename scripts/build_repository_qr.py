"""Generate a vector QR code for the presentation repository (ReportLab)."""
from pathlib import Path
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

URL = "https://github.com/MathisRost/agentic-ai-math"
OUT = Path(__file__).resolve().parents[1] / "assets" / "repository_qr.pdf"
qr = QrCodeWidget(URL, barLevel="M", barBorder=4, barWidth=240, barHeight=240)
drawing = Drawing(240, 240)
drawing.add(qr)
renderPDF.drawToFile(drawing, str(OUT))
print(f"{OUT}: {URL}")
