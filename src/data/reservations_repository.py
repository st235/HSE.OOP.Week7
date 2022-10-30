from enum import Enum

from models.table import Table
from utils.singleton import singleton

@singleton
class ReservationsRepository:

    def __init__(self):
        self._tables = dict()
        self._bookings = dict()

    def tables(self):
        return list(self._tables.values())

    def is_booked(self, tid) -> bool:
        if tid not in self._tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid in self._bookings:
            return True

        return False

    def get_booking_info(self, tid):
        if tid not in self._tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid not in self._bookings:
            return None

        return self._bookings[tid]

    def add_table(self, title, seats) -> bool:
        if title in self._tables:
            return False

        table = Table(title, seats)
        self._tables[table.name] = table
        return True

    def delete_table(self, tid) -> bool:
        if tid not in self._tables:
            return False

        del self._bookings[tid]
        del self._tables[tid]
        return True

    def release(self, tid) -> bool:
        if tid not in self._tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid not in self._bookings:
            # Cannot release the table
            return False

        del self._bookings[tid]
        return True

    def book(self, tid, booking) -> bool:
        if tid not in self._tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid in self._bookings:
            return False

        self._bookings[tid] = booking
        return True
