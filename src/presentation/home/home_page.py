import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_booking.tables_booking_page import TablesBookingPage
from presentation.home.tables_management.tables_management_page import TablesManagementPage
from presentation.home.tables_status.tables_status_page import TablesStatusPage


class HomePage(BasePage):

    SESSION_KEY_SELECTED_CONTROLLER = 'session_key.home_page.selected_controller'

    def __init__(self):
        super().__init__()
        self._content_page = None

    def onCreate(self):
        if HomePage.SESSION_KEY_SELECTED_CONTROLLER in st.session_state:
            self._open_page(st.session_state[HomePage.SESSION_KEY_SELECTED_CONTROLLER])

    def onPrepareView(self):
        st.sidebar.title('Available pages:')

        self._add_page_to_sidebar('Book a table', TablesBookingPage)
        self._add_page_to_sidebar('Manage tables', TablesManagementPage)
        self._add_page_to_sidebar('Tables status', TablesStatusPage)

    def _add_page_to_sidebar(self, title, controller_class):
        if st.sidebar.button(title):
            st.session_state[HomePage.SESSION_KEY_SELECTED_CONTROLLER] = controller_class
            super().reload()

    def _open_page(self, controller_class):
        self._content_page = controller_class()
        self._content_page.create()
