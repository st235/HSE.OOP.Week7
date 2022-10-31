import streamlit as st

from presentation.base_page import BasePage
from presentation.home.tables_booking.tables_booking_page import TablesBookingPage
from presentation.home.tables_management.tables_management_page import TablesManagementPage
from presentation.home.tables_status.tables_status_page import TablesStatusPage


class HomePage(BasePage):
    """
    The root page of the application.
    Contains references to another web pages.

    This view does not have a controller: this has been made for the sake of simplicity as
    the page does not handle any business logic.
    """

    """Internal page state responsible for keeping track of the opened page."""
    SESSION_KEY_SELECTED_PAGE = 'session_key.home_page.selected_page'

    def __init__(self):
        super().__init__()
        self.__content_page = None

    def on_create(self):
        if HomePage.SESSION_KEY_SELECTED_PAGE in st.session_state:
            self._open_page(st.session_state[HomePage.SESSION_KEY_SELECTED_PAGE])

    def on_prepare_view(self):
        st.sidebar.title('Available pages:')

        self._add_page_to_sidebar('Book a table', TablesBookingPage)
        self._add_page_to_sidebar('Manage tables', TablesManagementPage)
        self._add_page_to_sidebar('Tables status', TablesStatusPage)

    def _add_page_to_sidebar(self, title: str, page_class):
        """
        Creates a button in the sidebar menu.
        User will be redirected to a new page when the button is clicked.

        :param title: page's title that will be displayed on a button
        :param page_class: page's class or any other factory method allowing us to create a new page instance
        """
        if st.sidebar.button(title):
            st.session_state[HomePage.SESSION_KEY_SELECTED_PAGE] = page_class
            super().reload()

    def _open_page(self, page_class):
        """
        Opens the give page.
        When the page is opened the content of the home page will be replaced with a content
        of the child.

        :param page_class: page's class or any other factory method allowing is to create a new page instance
        """
        self.__content_page = page_class()
        self.__content_page.create()
