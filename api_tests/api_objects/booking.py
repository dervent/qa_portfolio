from datetime import date


class BookingDates:
    """
    Booking dates object.
    """
    def __init__(self, checkin: date = None, checkout: date = None) -> None:
        self.checkin = str(checkin)
        self.checkout = str(checkout)

    def get_dict(self) -> dict:
        """
        Return object as dict.
        """
        return {key: value for key, value in self.__dict__.items() if value is not None}


class Booking:
    """
    Booking object.
    """
    def __init__(self,
                 firstname: str = None,
                 lastname: str = None,
                 totalprice: float = None,
                 depositpaid: float = None,
                 bookingdates: BookingDates = None,
                 additionalneeds: str = None) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.bookingdates = bookingdates.get_dict() if bookingdates else None
        self.additionalneeds = additionalneeds

    def get_dict(self) -> dict:
        """
        Return object as dict.
        """
        return {key: value for key, value in self.__dict__.items() if value is not None}
