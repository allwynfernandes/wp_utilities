import pandas as pd
import streamlit as st
import xlsxwriter
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb


def get_pd_df(file):
    return pd.read_excel(file, engine='openpyxl')

def get_column_names(df):
    return list(df.columns)



def get_split_df_list(df, splitOnCol):
    group_set_collection = [group_set for group_set in df.groupby(by=splitOnCol)]
    return group_set_collection


def main():
    pass
if __name__ == '__main__':
    main()


def parse_df_to_excel():

    output = BytesIO()

    # Write files to in-memory strings using BytesIO
    # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Hello')
    workbook.close()



def parse_df_to_excel_easy(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data