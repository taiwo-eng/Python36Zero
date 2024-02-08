import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {invoice_nr}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Date: {invoice_date}', ln=1)

    excel_dataframe = pd.read_excel(filepath, sheet_name='Sheet 1')

    headers = excel_dataframe.columns
    headers = [item.replace('_', ' ').title() for item in headers]

    # Add headers
    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=60, h=8, txt=headers[1], border=1)
    pdf.cell(w=40, h=8, txt=headers[2], border=1)
    pdf.cell(w=30, h=8, txt=headers[3], border=1)
    pdf.cell(w=30, h=8, txt=headers[4], border=1, ln=1)

    # Add rows
    for index, row in excel_dataframe.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']),  border=1)
        pdf.cell(w=60, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    total_sum = excel_dataframe['total_price'].sum()
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=60, h=8, txt='', border=1)
    pdf.cell(w=40, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum
    pdf.set_font(family='Times', size=10)
    pdf.cell(w=30, h=8, txt=f'The total price is {total_sum}', ln=1)

    # Add company name and logo
    pdf.set_font(family='Times', size=10)
    pdf.cell(w=30, h=8, txt='Company Name')
    # pdf.image('filepath to image', w=10)

    pdf.output(f'PDFs/{filename}.pdf')
