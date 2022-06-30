import datetime
import streamlit as st

from sub_modules import investment_splitter
from sub_modules.aipl_reports import automations
def main_page():

    st.set_page_config(page_icon="🛠️", page_title="Wallace Data Processing Utility")

    selected_report = st.selectbox(
        'Which Utility would you like to use?',
        ('Investment Splitter', 'DCR Generator', 'Input Upload Converter'))

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
        
    if selected_report == 'Input Upload Converter':
        pass


def main():
    pass


if __name__ == '__main__':
        main()
