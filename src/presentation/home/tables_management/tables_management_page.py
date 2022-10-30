import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_management.tables_management_controller import TablesManagementController


class TablesManagementPage(BasePage):
    def __init__(self):
        super().__init__(TablesManagementController(self))

    def onPrepareView(self):
        st.title('Table management')
        self._build_tables_control_section()
        self._build_new_table_section()

    def _build_tables_control_section(self):
        st.header('Control existing tables')
        title = st.selectbox('Tables', [t.name for t in super().controller.get_tables()])

        col1, col2, col3 = st.columns(3)

        if col1.button('Take the table'):
            super().controller.take_the_table(title)

        if col2.button('Release the table'):
            super().controller.release_the_table(title)

        if col3.button('Delete'):
            super().controller.delete_table(title)

    def _build_new_table_section(self):
        with st.form('create_new_table', clear_on_submit=True):
            st.header('Create a new table')
            title = st.text_input('Table name', max_chars=64, placeholder='Table#4')
            seats = st.number_input('Seats available', min_value=1, max_value=20)

            if st.form_submit_button('Submit'):
                super().controller.create_table(title, seats)
