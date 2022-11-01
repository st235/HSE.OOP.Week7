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

    def get_available_tables(self):
        """
        Gets all available tables at the moment.
        If a table is booked it won't be displayed.
        """
        return list(filter(lambda table: not self.__tables_repository.is_booked(table.name),
                           self.__tables_repository.tables))

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
            self.__view.submit_error('Table does not exist')
            return

        if name is None or len(name) == 0 or phone is None or len(phone) == 0:
            self.__view.submit_error("Given data is invalid: (name = '{}', phone = '{}')".format(name, phone))
            return

        if self.__tables_repository.book(table_title, Booking(name, phone, get_time(datetime), period)):
            self.__view.reload()
        else:
            self.__view.submit_error('The table can\'t be booked. Perhaps, there is another booking?')
