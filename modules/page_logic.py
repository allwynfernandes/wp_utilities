import datetime
import streamlit as st

from sub_modules import excel_splitter
from sub_modules import investment_splitter
from sub_modules.aipl_reports import automations
def main_page():

    st.set_page_config(page_icon="🛠️", page_title="Wallace Data Processing Utility")

    selected_report = st.selectbox(
        'Which Utility would you like to use?',
        ('Investment Splitter', 'DCR Generator', 'Input Upload Converter', 'Excel Splitter'))

    st.write('You selected:', selected_report)

    # ======== Investment Splitter ========
    if selected_report == 'Investment Splitter':
        with st.form("investment_splitter_fm"):
            st.write("🛠️ Wallace Data Processing Utility")
            investment_file =  st.file_uploader("Choose Investment Excel file: ")

                # Every form must have a submit button.
            st.info("Press 'Submit' to run the app")
            submitted = st.form_submit_button("Submit")

        if submitted:
            # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
            #     st.error("Incorrent columns in file uploaded")

            investment_table= investment_splitter.main_logic(raw_data=investment_file)


            st.success('Done!') 

            st.download_button(
            "Press to Download Investments Table",
            investment_table.to_csv(index=False).encode('utf-8'),
            f"{investment_splitter.get_timestamp()}_investments.csv",
            "text/csv",
            key='download-csv'
            )
            

            st.write("Investment Table")
            st.table(investment_table)



    # ======== DCR GENERATOR ===============
    if selected_report == 'DCR Generator':
        with st.form("dcr_generator_fm"):
            st.write("🛠️ Wallace Data Processing Utility")
            st.write("🛠️ DCR Generator")

            fromDate = st.date_input(
                "Enter Report From date",
                datetime.date(2022, 6, 10))
            toDate = st.date_input(
                "Enter Report From date",
                datetime.date(2022, 6, 20))    

                # Every form must have a submit button.
            st.info("Press 'Submit' to run the app")
            submitted = st.form_submit_button("Submit")

        if submitted:
            # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
            #     st.error("Incorrent columns in file uploaded")
            with st.spinner("Generating report: 5 mins..."):
                dcr_table= automations.get_all_div_dcr_submission(fromDt=fromDate, toDt=toDate)


            st.success('Done!') 

            st.download_button(
            "Press to Download Investments Table",
            dcr_table.to_csv(index=False).encode('utf-8'),
            f"{investment_splitter.get_timestamp()}_combine_dcr.csv",
            "text/csv",
            key='download-csv'
            )
            

            st.write("DCR Table Sample")
            st.table(dcr_table.head(3))

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
