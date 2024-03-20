import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

invoices = glob.glob("invoices/*.xlsx")

for invoice in invoices:

    # Initiate PDF
    df = pd.read_excel(invoice, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Filename as list.
    filename = Path(invoice).stem
    file_number, file_date = filename.split('-')

    # Layout
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {file_number}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {file_date}", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
