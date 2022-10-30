class Table:
    def __init__(self, name, seats):
        self._name = name
        self._seats = seats

    @property
    def name(self):
        return self._name

    @property
    def seats(self):
        return self._seats
