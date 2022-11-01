class Booking:
    """
    Booking representation, contains of: user's name, user's phone, booking time and an interval of the booking.
    """

    def __init__(self, name, phone, time, period):
        self.__name = name
        self.__phone = phone
        self.__time = time
        self.__period = period

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def time(self):
        return self.__time

    @property
    def period(self):
        return self.__period
