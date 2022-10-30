import streamlit as st

class BasePage:

    def __init__(self, controller=None):
        self._controller = controller

    @property
    def controller(self):
        return self._controller

    def create(self):
        self.onCreate()
        self.onPrepareView()

    def reload(self):
        st.experimental_rerun()

    def onCreate(self):
        pass

    def onPrepareView(self):
        pass

    def show_error(self, description):
        st.error(description)

    def show_success(self, description):
        st.success(description)
