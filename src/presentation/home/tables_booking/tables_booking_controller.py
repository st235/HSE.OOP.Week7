from data.reservations_repository import ReservationsRepository


class TablesBookingController:
    def __init__(self, view, reservations_repository=ReservationsRepository()):
        self._view = view
        self._reservations_repository = reservations_repository

    def get_tables(self):
        return self._reservations_repository.tables()
