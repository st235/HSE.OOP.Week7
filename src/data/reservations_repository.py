from enum import Enum

from models.table import Table
from utils.singleton import singleton


@singleton
class ReservationsRepository:

    class AvailabilityType(Enum):
        AVAILABLE = 0
        BUSY = 1

    def __init__(self):
        self._tables = dict()
        self._bookings = dict()

    def tables(self):
        return list(self._tables.values())

    def status(self, tid) -> AvailabilityType:
        if tid not in self._tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid in self._bookings:
            return ReservationsRepository.AvailabilityType.BUSY

        return ReservationsRepository.AvailabilityType.AVAILABLE

    def add_table(self, title, seats) -> bool:
        if title in self._tables:
            return False

        table = Table(title, seats)
        self._tables[table.name] = table
        return True

    def delete_table(self, tid) -> bool:
        if tid not in self._tables:
            return False

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

    def book(self, table, booking) -> bool:
        # table id
        tid = table.name

        if tid not in self._tables:
            raise Exception('Table with id {} does not exist'.format(tid))

        if tid in self._bookings:
            return False

        self._bookings[tid] = booking
        return True
