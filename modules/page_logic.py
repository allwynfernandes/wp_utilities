import datetime
import streamlit as st


from sub_modules import excel_splitter
from sub_modules import investment_splitter
from sub_modules.aipl_reports import automations
from sub_modules.aipl_reports.utils import commons



def main_page():

    st.set_page_config(page_icon="🛠️", page_title="Wallace Data Processing Utility")

    selected_report = st.selectbox(
        'Which Utility would you like to use?',
        ('SAS Splitter', 'MyWallace Report Generator', 'MyWallace Excel Generator', 'Input Upload Converter', 'Excel Splitter'))

    st.write('You selected:', selected_report)

    # ======== SAS Splitter ========
    if selected_report == 'SAS Splitter':
        with st.form("SAS_splitter_fm"):
            st.write("🛠️ Wallace Data Processing Utility")
            investment_file =  st.file_uploader("Choose SAS Excel file: ")

                # Every form must have a submit button.
            st.info("Press 'Submit' to run the app")
            submitted = st.form_submit_button("Submit")

        if submitted:
            # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
            #     st.error("Incorrent columns in file uploaded")

            investment_table= investment_splitter.main_logic(raw_data=investment_file)


            st.success('Done!') 

            st.download_button(
            "Press to Download SAS Table",
            investment_table.to_csv(index=False).encode('utf-8'),
            f"{investment_splitter.get_timestamp()}_SAS.csv",
            "text/csv",
            key='download-csv'
            )
            

            st.write("SAS Table")
            st.table(investment_table)



    # ======== MyWallace GENERATOR ===============
    if selected_report == 'MyWallace Report Generator':
        with st.form("dcr_generator_fm"):
            st.write("🛠️ Wallace Data Processing Utility") 
            st.write("🛠️ DCR Generator")

            selected_report = st.selectbox(
                label='Select report to generate',
                options=['dcr', 'stp', 'mtp'],
                key='select-aipl-report' )
            fromDate = st.date_input(
                "Enter Report From date",
                commons.get_default_dates('datetime')[0])
            toDate = st.date_input(
                "Enter Report To date",
                commons.get_default_dates('datetime')[1])    



                # Every form must have a submit button.
            st.info("Press 'Submit' to run the app")
            submitted = st.form_submit_button("Submit")

        if submitted:
            # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
            #     st.error("Incorrent columns in file uploaded")
            with st.spinner("Generating report: 5 mins..."):
                dcr_table= automations.get_report_general(reportName=selected_report, fromDt=fromDate, toDt=toDate)


            st.success('Done!') 

            st.download_button(
           f"Press to Download {selected_report} Table",
            dcr_table.to_csv(index=False).encode('utf-8'),
            f"{investment_splitter.get_timestamp()}_combine_{selected_report}_{str(fromDate)}_TO_{str(toDate)}.csv",
            "text/csv",
            key='download-csv'
            )
            

            st.write(f"{selected_report} Table Sample")
            st.table(dcr_table.head(3))


    # ======== MyWallace EXCEL  ===============
    if selected_report == 'MyWallace Excel Generator':
        with st.form("excel_generator_fm"):
            st.write("🛠️ Wallace Data Processing Utility") 
            st.write("🛠️ Excel Report Generator")

            selected_report = st.selectbox(
                label='Select excel report to generate',
                options=['dcr_excel'],
                key='select-aipl-excel-report' )
            fromDate = st.date_input(
                "Enter Report From date",
                commons.get_default_dates('datetime')[0])
            toDate = st.date_input(
                "Enter Report To date",
                commons.get_default_dates('datetime')[1])    



                # Every form must have a submit button.
            st.info("Press 'Submit' to run the app")
            submitted = st.form_submit_button("Submit")

        if submitted:
            # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
            #     st.error("Incorrent columns in file uploaded")
            with st.spinner("Generating report: 5 mins..."):
                data_table = automations.get_excel_general(excelName=selected_report, fromDt=fromDate, toDt=toDate)


            st.success('Done!') 

        #     st.download_button(
        #    f"Press to Download {selected_report} Table",
        #     data_table.to_csv(index=False).encode('utf-8'),
        #     f"{investment_splitter.get_timestamp()}_combine_{selected_report}_{str(fromDate)}_TO_{str(toDate)}.csv",
        #     "text/csv",
        #     key='download-csv'
        #     )
        
            st.download_button(
            label=f"Press to Download {selected_report} Table",
            data=data_table, #group[1].to_csv(index=False).encode('utf-8'),
            file_name=f"{investment_splitter.get_timestamp()}_{selected_report}_report.xlsx",
            # "text/csv",
            key=f'{selected_report}-excel-download'
            )
            # st.write(f"{selected_report} Table Sample")
            # st.table(data_table.head(3))

            

    # =========== EXCEL SPLITTER =============

    if selected_report == 'Excel Splitter':
        st.caption('Place the column to be split on as FIRST column.')
        st.caption('Only select EXCEL file.')

        with st.form("excel_splitter"):
            st.write("🛠️ Wallace Data Processing Utility")
            st.write("🛠️ Excel Splitter")

            file_to_split =  st.file_uploader("Choose Excel File to split: ")

            st.info("Press 'Submit' to proceed")
            submitted = st.form_submit_button("Submit")

        if submitted:
            # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
            #     st.error("Incorrent columns in file uploaded")
            with st.spinner("Reading excel file: 5 mins..."):
                to_split_df= excel_splitter.get_pd_df(file_to_split)
                df_cols = tuple(excel_splitter.get_column_names(to_split_df))

            st.write("Excel Table Sample")
            st.table(to_split_df.head(3))


            selected_column = st.selectbox(
                label='Select column to split on?',
                options=df_cols,
                key='select-col-to-split-on' )


            group_set_collection = excel_splitter.get_split_df_list(to_split_df, selected_column)
            group = group_set_collection[0]
            for group in group_set_collection:
                ready_excel = excel_splitter.parse_df_to_excel_easy(group[1])
                st.download_button(
                label=f"Press to Download {group[0]} Table",
                data=ready_excel, #group[1].to_csv(index=False).encode('utf-8'),
                file_name=f"{investment_splitter.get_timestamp()}_{group[0]}_excel_splitter.xlsx",
                # "text/csv",
                key=f'{group[0]}-csv-download'
                )
                

            # st.write("DCR Table Sample")
            # st.table(dcr_table.head(3))

    if selected_report == 'Input Upload Converter':
        pass


def main():
    pass


if __name__ == '__main__':
        main()
