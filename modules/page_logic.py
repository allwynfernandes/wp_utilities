from utils import helpers
import streamlit as st
def main_page():

    st.set_page_config(page_icon="🛠️", page_title="Wallace Data Processing Utility")

    with st.form("my_form"):
        st.write("🛠️ Wallace Data Processing Utility")
        investment_file =  st.file_uploader("Choose Investment Excel file: ")

            # Every form must have a submit button.
        st.info("Press 'Submit' to run the app")
        submitted = st.form_submit_button("Submit")

    if submitted:
        # if  not(investment_file.columns == ['Division', 'Mobile', 'Investment']):
        #     st.error("Incorrent columns in file uploaded")

        investment_table= helpers.main_logic(raw_data=investment_file)


        st.success('Done!') 

        st.download_button(
        "Press to Download Investments Table",
        investment_table.to_csv(index=False).encode('utf-8'),
        f"{helpers.get_timestamp()}_investments.csv",
        "text/csv",
        key='download-csv'
        )
        

        st.write("Investment Table")
        st.table(investment_table)



def main():
    pass


if __name__ == '__main__':
        main()
