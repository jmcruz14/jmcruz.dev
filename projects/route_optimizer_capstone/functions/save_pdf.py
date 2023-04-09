import pandas as pd
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

def save_pdf(dataframe):

    dataframe_length = len(dataframe)
    print(dataframe_length)
    dict_from_df = dataframe.to_dict()
    df_col_length = len(dict_from_df) # 3

    pdf = FPDF(orientation="L", unit="mm", format="A4")
    
    page_width = pdf.w - 2 * pdf.l_margin
    col_width = page_width/df_col_length 

    pdf.add_page()
    pdf.set_font('Helvetica', size=12)

    for column in dict_from_df.keys():
        pdf.cell(col_width, 12, column, border = 1, new_x = XPos.RIGHT)
    pdf.cell(col_width, 12, " ", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    print(dict_from_df.keys())

    for i in range(0, dataframe_length):
        for column in dict_from_df.keys():
            pdf.multi_cell(col_width, 10, str(dict_from_df[column][i]), border=1, new_x=XPos.RIGHT, new_y=YPos.LAST)
        pdf.multi_cell(col_width, 10, "", new_x = XPos.LMARGIN, new_y=YPos.NEXT)
    
    # Turn into string
    pdf = pdf.output(dest='S')
    pdf = pdf.decode('latin-1')
    
    return pdf