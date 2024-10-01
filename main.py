from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', format='A4', unit='mm')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(265)
    #Set footer for master page
    pdf.set_font(family='Times', size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    #x1, y1, x2, y2 are the distance of starting and finishhing
    #points of line from top and sides

    for i in range(row['Pages']):
        pdf.add_page()
        #Set footer for other pages
        pdf.ln(277)
        pdf.set_font(family='Times', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output('output.pdf')
