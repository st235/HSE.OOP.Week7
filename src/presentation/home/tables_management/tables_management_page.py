import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_management.tables_management_controller import TablesManagementController


class TablesManagementPage(BasePage):
    """
    Table management page: user can see current tables, create new, take or release table.
    """

    def __init__(self):
        super().__init__(TablesManagementController(self))

    def on_prepare_view(self):
        st.title('Table management')
        self.__build_tables_controls_section()
        self.__build_new_table_section()

    def __build_tables_controls_section(self):
        """
        Builds existing tables controls section: delete, take, or release table.
        """
        tables = super().controller.get_tables()
        has_no_tables = len(tables) == 0

        st.header('Control existing tables')
        title = st.selectbox('Tables', [t.name for t in tables])

        col_left, col_middle, col_right = st.columns(3)

        if col_left.button('Take the table', disabled=has_no_tables):
            super().controller.take_table(title)

        if col_middle.button('Release the table', disabled=has_no_tables):
            super().controller.release_table(title)

        if col_right.button('Delete', disabled=has_no_tables):
            super().controller.delete_table(title)

    def __build_new_table_section(self):
        """
        Builds a section to create a new table.
        """
        with st.form('create_new_table', clear_on_submit=True):
            st.header('Create a new table')
            title = st.text_input('Table name', max_chars=64, placeholder='Table#4')
            seats = st.number_input('Seats available', min_value=1, max_value=20)

            if st.form_submit_button('Submit'):
                super().controller.create_table(title, seats)
