from typing import Optional

from models.booking import Booking
from models.table import Table
from utils.singleton import singleton


@singleton
class TablesRepository:
    """
    Handles all operations with tables: get, add, delete, book, release and so on.
    Should be a singleton as handles everything in memory.
    """

    def __init__(self):
        self.__tables = dict()
        self.__bookings = dict()

    @property
    def tables(self):
        """
        Gets all available tables
        :return: list of tables
        """
        return list(self.__tables.values())

    def is_booked(self, tid: str) -> bool:
        """
        Checks if the given table is booked. If the table is booked return True and False otherwise.

        :param tid: unique id of the title, usually, title is used.
        """
        if tid not in self.__tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid in self.__bookings:
            return True

        return False

    def get_booking_info(self, tid: str) -> Optional[Booking]:
        """
        Gets booking information for the given table.

        :param tid: unique table id, usually, title is used
        :return: an optional value of booking
        """
        if tid not in self.__tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid not in self.__bookings:
            return None

        return self.__bookings[tid]

    def create(self, title: str, seats: int) -> bool:
        """
        Creates a table and adds it to the tables list.

        :param title: new unique name, if  non-unique False is returned
        :param seats: amount of seats
        """
        if title in self.__tables:
            return False

        table = Table(title, seats)
        self.__tables[table.name] = table
        return True

    def delete(self, tid: str) -> bool:
        """
        Deleted the given table.
        """
        if tid not in self.__tables:
            return False

        if tid in self.__bookings:
            del self.__bookings[tid]
        del self.__tables[tid]
        return True

    def release(self, tid: str) -> bool:
        """
        Releases given table even if the table has been booked by another person.
        """
        if tid not in self.__tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid not in self.__bookings:
            # Cannot release the table
            return False

        del self.__bookings[tid]
        return True

    def book(self, tid, booking) -> bool:
        """
        Books the given table for a given period if time.
        If the table is already booked False is returned.
        Double booking are not allowed.
        """
        if tid not in self.__tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid in self.__bookings:
            return False

        self.__bookings[tid] = booking
        return True
