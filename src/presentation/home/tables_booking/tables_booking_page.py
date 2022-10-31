import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_booking.tables_booking_controller import TablesBookingController


class TablesBookingPage(BasePage):
    """
    A web page representing a table booking flow.
    """
    def __init__(self):
        super().__init__(TablesBookingController(self))

    def on_prepare_view(self):
        with st.form('book_a_table'):
            st.title('Tables Booking')

            name = st.text_input('Name', max_chars=64)
            phone = st.text_input('Phone', max_chars=32)

            col_left, col_right = st.columns(2)

            with col_left:
                time = st.time_input('From')

            with col_right:
                period = st.number_input('Period', min_value=30, max_value=180, step=30, format="%d")

            tables = super().controller.get_tables()
            has_no_tables = len(tables) == 0

            # table id
            tid = st.selectbox('Tables', [t.name for t in tables])

            if st.form_submit_button('Submit', disabled=has_no_tables):
                super().controller.book_table(tid, name, phone, time, period)





