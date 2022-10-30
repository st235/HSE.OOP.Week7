import pandas as pd

from data.reservations_repository import ReservationsRepository


class TablesStatusController:
    def __init__(self, view, reservations_repository=ReservationsRepository()):
        self._view = view
        self._reservations_repository = reservations_repository

    def populate_tables_info(self):
        tables = self._reservations_repository.tables()
        statuses = [('Booked' if self._reservations_repository.is_booked(table.name) else 'Free') for table in tables]

        tables_with_statuses = dict()
        tables_with_statuses['table'] = [t.name for t in tables]
        tables_with_statuses['seats'] = [t.seats for t in tables]
        tables_with_statuses['status'] = statuses
        tables_with_statuses['booking info'] = [self._prepare_booking_info(self._reservations_repository.get_booking_info(t.name)) for t in tables]

        return pd.DataFrame(tables_with_statuses)

    def _prepare_booking_info(self, booking):
        if booking is None:
            return "N/A"

        hours = int(booking.time) // 60
        minutes = int(booking.time) % 60
        return "by {}\nphone: {}\nmade for: {:02d}:{:02d}".format(booking.name, booking.phone, hours, minutes)
