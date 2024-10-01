from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', format='A4', unit='mm')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=14, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 21, 200, 21)
    #x1, y1, x2, y2 are the distance of starting and finishhing
    #points of line from top and sides
    for i in range(row['Pages']):
        pdf.add_page()

pdf.output('output.pdf')
