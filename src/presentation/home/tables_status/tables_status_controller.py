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
        bookings = [self.__tables_repository.get_booking_info(t.name) for t in tables]

        statuses = [('Booked' if self.__tables_repository.is_booked(table.name) else 'Free') for table in tables]

        tables_with_statuses = dict()
        tables_with_statuses['table'] = [t.name for t in tables]
        tables_with_statuses['seats'] = [t.seats for t in tables]
        tables_with_statuses['status'] = statuses
        tables_with_statuses['booked by'] = [(booking.name if booking is not None else '') for booking in bookings]
        tables_with_statuses['phone'] = [(booking.phone if booking is not None else '') for booking in bookings]
        tables_with_statuses['from'] = [self.__get_booking_start_time(booking) for booking in bookings]
        tables_with_statuses['till'] = [self.__get_booking_end_time(booking) for booking in bookings]

        return pd.DataFrame(tables_with_statuses)

    def __get_booking_start_time(self, booking: Booking) -> str:
        """
        Gets booking time in human-readable format
        """
        if booking is None:
            return ''

        hours, minutes = get_hours_and_minutes(booking.time)
        return "{:02d}:{:02d}".format(hours, minutes)

    def __get_booking_end_time(self, booking: Booking) -> str:
        """
        Gets booking time in human-readable format
        """
        if booking is None:
            return ''

        if booking.period == -1:
            return 'The end of the day'

        hours, minutes = get_hours_and_minutes(booking.time + booking.period)
        return "{:02d}:{:02d}".format(hours, minutes)
