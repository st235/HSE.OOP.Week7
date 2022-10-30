from data.reservations_repository import ReservationsRepository
from models.booking import Booking
from utils.time import get_time


class TablesBookingController:
    def __init__(self, view, reservations_repository=ReservationsRepository()):
        self._view = view
        self._reservations_repository = reservations_repository

    def get_tables(self):
        return self._reservations_repository.tables()

    def book_the_table(self, tid, name, phone, datetime, period):
        if tid is None or len(tid) == 0:
            self._view.show_error('Table should exist')
            return

        if self._reservations_repository.book(tid, Booking(name, phone, get_time(datetime), period)):
            self._view.show_success('The table has been successfully booked')
        else:
            self._view.show_error('The table can\'t be booked. Perhaps, there is another booking?')
