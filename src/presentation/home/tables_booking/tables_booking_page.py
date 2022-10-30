import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_booking.tables_booking_controller import TablesBookingController


class TablesBookingPage(BasePage):
    def __init__(self):
        super().__init__(TablesBookingController(self))

    def onPrepareView(self):
        with st.form('book_a_table'):
            st.title('Tables Booking')

            name = st.text_input('Name')
            phone = st.text_input('Phone')

            col1, col2 = st.columns(2)

            with col1:
                time = st.time_input('From')

            with col2:
                period = st.number_input('Period')

            # table id
            tid = st.selectbox('Tables', [t.name for t in super().controller.get_tables()])

            if st.form_submit_button('Submit'):
                super().controller.book_the_table(tid, name, phone, time, period)





