from data.tables_repository import TablesRepository
from models.booking import Booking
from utils.time import get_time


class TablesBookingController:
    """
    Controls logic related to tables booking.
    """

    def __init__(self, view, tables_repository=TablesRepository()):
        self.__view = view
        self.__tables_repository = tables_repository

    def get_tables(self):
        """
        Gets all available tables.
        """
        return self.__tables_repository.tables

    def book_table(self, table_title: str, name: str, phone: str, datetime, period: int):
        """
        Books the given table with the given information.

        :param table_title: table unique title (id)
        :param name: user name
        :param phone: user phone
        :param datetime: booking start date
        :param period: a period of booking, the end of the booking can be calculated using the period as
        final_date = start_date + period
        """
        if table_title is None or len(table_title) == 0:
            self.__view.submit_error('Table should exist')
            return

        if self.__tables_repository.book(table_title, Booking(name, phone, get_time(datetime), period)):
            self.__view.submit_success('The table has been successfully booked')
        else:
            self.__view.submit_error('The table can\'t be booked. Perhaps, there is another booking?')
