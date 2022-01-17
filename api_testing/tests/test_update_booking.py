from api_testing.resources.test_base import TestBase
from unittest import skip


class TestUpdateBooking(TestBase):
    """
    Class for testing the update of bookings
    """
    base = TestBase()

    @classmethod
    def setUpClass(cls):
        """
        Authenticate admin user; create new booking
        """
        cls.base.create_token()
        cls.original_booking = cls.base.create_booking().json()
        cls.booking_id = cls.original_booking["bookingid"]
        dates = cls.base.get_dates(21, 5)
        cls.new_booking_data = {
            "firstname": "API",
            "lastname": "Testing",
            "totalprice": 400,
            "depositpaid": False,
            "bookingdates": {
                "checkin": dates["checkIn"],
                "checkout": dates["checkOut"]
            },
            "additionalneeds": "None"
        }

    def test_update_booking_success(self):
        """
        Test successful update of existent booking
        """
        response = self.base.update_booking(self.booking_id, self.new_booking_data)

        # Verify that actual booking data is updated
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())
        self.assertFalse(self.is_dict_identical(self.original_booking, response.json()))
        self.assertTrue(self.is_dict_identical(self.new_booking_data, response.json()))

    def test_update_booking_partial_data_failure(self):
        """
        Test failure to update existent booking with partial data
        """
        response = self.base.update_booking(
            self.booking_id, {"bookingdates": self.new_booking_data["bookingdates"]})

        self.assertEqual(400, response.status_code)
        self.assertEqual("Bad Request", response.text)

    @skip("Bug: API does not properly handle requests with nonexistent booking IDs.")
    def test_update_booking_nonexistent_id_failure(self):
        """
        Test failure to update a nonexistent booking
        """
        response = self.base.update_booking("invalidID", self.new_booking_data)

        self.assertEqual(404, response.status_code)
        self.assertEqual("Not Found", response.text)
