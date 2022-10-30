import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_status.tables_status_controller import TablesStatusController


class TablesStatusPage(BasePage):
    def __init__(self):
        super().__init__(TablesStatusController())

    def onPrepareView(self):
        st.write('Hello from tables status page')
