class Booking:
    def __init__(self, name, phone, time, interval):
        self._name = name
        self._phone = phone
        self._time = time
        self._interval = interval

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def time(self):
        return self._time
