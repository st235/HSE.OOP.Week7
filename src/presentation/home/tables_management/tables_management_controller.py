from data.reservations_repository import ReservationsRepository
from models.booking import Booking
from utils.time import get_current_time


class TablesManagementController:
    def __init__(self, view, reservations_repository=ReservationsRepository()):
        self._view = view
        self._reservations_repository = reservations_repository

    def get_tables(self):
        return self._reservations_repository.tables()

    def create_table(self, title, seats):
        if title is None or len(title) == 0 or seats <= 0 or seats > 30:
            self._view.show_error('Given title {} or seats {} are invalid'.format(title, seats))
            return

        if self._reservations_repository.add_table(title, seats):
            self._view.reload()
        else:
            self._view.show_error('Table with name \'{}\' already exists'.format(title))

    def delete_table(self, title):
        if title is None or len(title) == 0:
            self._view.show_error('Table should exist')
            return

        if self._reservations_repository.delete_table(title):
            self._view.reload()
        else:
            self._view.show_error('The table with name {} does not exist'.format(title))

    def take_the_table(self, title):
        if title is None or len(title) == 0:
            self._view.show_error('Table should exist')
            return

        if self._reservations_repository.book(title, Booking('Staff', 'N/A', get_current_time(), -1)):
            self._view.show_success('The table has been successfully booked')
        else:
            self._view.show_error('The table can\'t be booked. Perhaps, there is another booking?')

    def release_the_table(self, title):
        if title is None or len(title) == 0:
            self._view.show_error('Table should exist')
            return

        if self._reservations_repository.release(title):
            self._view.show_success('The table has been successfully released')
        else:
            self._view.show_error('The table can\'t be released. Perhaps, it was not booked?')

