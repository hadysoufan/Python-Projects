from fpdf import FPDF
import pandas as pd


def footer():
    """
    Add a footer to the PDF document.

    Draws a horizontal line at the bottom of the page and adds the 'Topic' text
    in italics at the right-aligned position.
    """
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for i, row in df.iterrows():
    """
    Iterate over each row in the DataFrame and generate a PDF page for each topic.

    - Add a new page to the PDF document.
    - Set the font style, size, and color for the topic title.
    - Draw a horizontal line below the topic title.
    - Add a footer to the page.
    - If the 'Pages' column value is greater than 1, add additional pages with the same footer.
    """
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 25, 200, 25)

    footer()

    for j in range(row['Pages'] - 1):
        pdf.add_page()
        footer()

pdf.output('output.pdf')
