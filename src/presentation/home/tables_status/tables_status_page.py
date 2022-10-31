import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_status.tables_status_controller import TablesStatusController


class TablesStatusPage(BasePage):
    """
    Status page: shows a list of tables with their availability and associated booking information.
    """

    def __init__(self):
        super().__init__(TablesStatusController(self))

    def on_prepare_view(self):
        st.title('Tables status')
        st.table(super().controller.populate_tables_info())
