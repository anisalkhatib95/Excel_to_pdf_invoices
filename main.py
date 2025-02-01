import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=12, txt=f"Invoice #{invoice_no}")
    pdf.output(f"PDFs/{filename}.pdf")