class Table:
    """
    Representation of a table, consists of: name and available seats.
    """

    def __init__(self, name, seats):
        self._name = name
        self._seats = seats

    @property
    def name(self):
        return self._name

    @property
    def seats(self):
        return self._seats
