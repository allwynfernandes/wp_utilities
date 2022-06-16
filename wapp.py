import logging
import datetime
from modules import page_logic
import streamlit as st


timestamp = datetime.datetime.now().strftime('%b-%d-%H%M%S')
logging.basicConfig(filename=f'debug/webapp_debug_{timestamp}.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

def main():
    page_logic.main_page()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.debug(e)
        st.exception(e)
