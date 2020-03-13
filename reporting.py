import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF

df = pd.DataFrame()
df['Question'] = ['age', 'bp', 'sg', 'al', 'su', 'rbc_normal', 'pc_normal', 'pcc_present',
       'ba_present', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc',
       'rc', 'htn_yes', 'dm_yes', 'cad_yes', 'appet_poor', 'pe_yes', 'ane_yes']
def reporter(outputs):
    df['Your_Inputs'] = outputs
    title("Your Report")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Just a report", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.cell(50, 10, 'Question', 1, 0, 'C')
    pdf.cell(40, 10, 'Ans', 1, 0, 'C')
    pdf.cell(-90)
    pdf.set_font('arial', '', 12)
    for i in range(0, len(df)):
        pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(df['Your_Inputs'].iloc[i])), 1, 0, 'C')
        # pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
        pdf.cell(-90)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-30)
    pdf.output('application/static/data/report.pdf', 'F')
    return "done"