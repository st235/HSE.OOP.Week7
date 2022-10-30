import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_status.tables_status_controller import TablesStatusController


class TablesStatusPage(BasePage):
    def __init__(self):
        super().__init__(TablesStatusController(self))

    def onPrepareView(self):
        st.title('Status')
        st.table(super().controller.populate_tables_info())
