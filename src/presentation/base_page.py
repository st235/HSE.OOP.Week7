import streamlit as st


class BasePage:
    """
    Represents a base page in the system.
    All other pages should inherit this page
    in order to implement a common page lifecycle.
    """

    def __init__(self, controller=None):
        self.__controller = controller

    @property
    def controller(self):
        """
        Part of the MVC architecture.

        In this architecture a view - a page in our case - represents a hierarchy of the widgets
        that would be shown to users. Views do not handle sophisticated logic but take care of
        user input, views state, and drawing step.

        A controller, associated view a view, on the contrary takes care of the business logic of
        the application.

        Usually, every view should have a controller, opposite stands either.
        Controller's lifecycle is associated with view's lifecycle and does not over-live its original view.
        """
        return self.__controller

    def create(self):
        """
        Starts a web page lifecycle, consisting of 2 steps:
            1. created: means the web page has been prepared and soon will be displayed.
            This step can be used to initialise variables that should live as long as the page lives.
            2. prepared: means that the web page is completely prepared to be displayed and is asking
            to provide views hierarchy.
        """
        self.on_create()
        self.on_prepare_view()

    def on_create(self):
        """
        A web page has been created and will be shown soon.
        The web page did not have views hierarchy and should
        not care about it just yet. This step is dedicated to
        prepare some lifecycle-aware variables, for example,
        restore the web page state from a persistent storage.
        """
        pass

    def on_prepare_view(self):
        """
        A web page has been asked to prepare views hierarchy.
        This step signals to the web page that the drawing is
        going to happen soon.
        """
        pass

    def reload(self):
        """
        Asks the view to reload its view hierarchy.
        This call is delegated to streamlit as streamlit handles drawing step.
        """
        st.experimental_rerun()

    def submit_error(self, description: str):
        """
        Submits a message that explains the error to the current web page.

        :param description: human-readable description of the error.
        """
        st.error(description)

    def submit_success(self, description: str):
        """
        Submits a successful message to the web page.

        :param description: human-readable message.
        """
        st.success(description)
