import pandas as pd

from data.tables_repository import TablesRepository
from models.booking import Booking
from utils.time import get_hours_and_minutes


class TablesStatusController:
    """
    Handle business logic related to showing tables' statuses.
    """

    def __init__(self, view, tables_repository=TablesRepository()):
        self.__view = view
        self.__tables_repository = tables_repository

    def populate_tables_info(self):
        """
        Populates all necessary information about tables, like, name, seats available, availability, or current
        booking info.
        :return: prepared dataframe
        """
        tables = self.__tables_repository.tables
        statuses = [('Booked' if self.__tables_repository.is_booked(table.name) else 'Free') for table in tables]

        tables_with_statuses = dict()
        tables_with_statuses['table'] = [t.name for t in tables]
        tables_with_statuses['seats'] = [t.seats for t in tables]
        tables_with_statuses['status'] = statuses
        tables_with_statuses['booking info'] = \
            [self.__prepare_booking_info(self.__tables_repository.get_booking_info(t.name)) for t in tables]

        return pd.DataFrame(tables_with_statuses)

    def __prepare_booking_info(self, booking: Booking) -> str:
        """
        Represents a booking as a string.
        """
        if booking is None:
            return 'N/A'

        hours, minutes = get_hours_and_minutes(booking.time)
        return "by {} \nphone: {} \nmade for: {:02d}:{:02d}".format(booking.name, booking.phone, hours, minutes)
