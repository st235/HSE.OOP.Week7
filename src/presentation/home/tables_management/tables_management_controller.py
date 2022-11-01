from data.tables_repository import TablesRepository
from models.booking import Booking
from utils.time import get_current_time


class TablesManagementController:
    def __init__(self, view, tables_repository=TablesRepository()):
        self.__view = view
        self.__tables_repository = tables_repository

    def get_tables(self):
        return self.__tables_repository.tables

    def create_table(self, title: str, seats: int):
        """
        Creates a table. If it cannot create a table will send an error message
        to the view, and successful message otherwise.

        :param title: unique title of the table
        :param seats: available seats count
        """
        if title is None or len(title) == 0 or seats <= 0 or seats > 30:
            self.__view.submit_error("The given data is invalid:(title='{}', seats='{}')".format(title, seats))
            return

        if self.__tables_repository.create(title, seats):
            self.__view.reload()
        else:
            self.__view.submit_error('Table with name \'{}\' already exists'.format(title))

    def delete_table(self, title: str):
        """
        Deletes a table with a given unique title.
        """
        if title is None or len(title) == 0:
            self.__view.submit_error('Table should exist')
            return

        if self.__tables_repository.delete(title):
            self.__view.reload()
        else:
            self.__view.submit_error('The table with name {} does not exist'.format(title))

    def take_table(self, title: str):
        """
        Takes a table with the given unique title. If the table has been already taken
        shows error.
        """
        if title is None or len(title) == 0:
            self.__view.submit_error('Table should exist')
            return

        if self.__tables_repository.book(title, Booking('Staff', 'N/A', get_current_time(), -1)):
            self.__view.submit_success('The table has been successfully booked')
        else:
            self.__view.submit_error('The table can\'t be booked. Perhaps, there is another booking?')

    def release_table(self, title: str):
        """
        Releases a table with the given title. If the table has not been already booked
        will show error.
        """
        if title is None or len(title) == 0:
            self.__view.submit_error('Table should exist')
            return

        if self.__tables_repository.release(title):
            self.__view.submit_success('The table has been successfully released')
        else:
            self.__view.submit_error('The table can\'t be released. Perhaps, it was not booked?')

