import pandas as pd
import glob

invoices = glob.glob("invoices/*.xlsx")

for invoice in invoices:
    df = pd.read_excel(invoice, sheet_name="Sheet 1")
    print(df)
