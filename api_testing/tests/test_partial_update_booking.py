from api_testing.resources.test_base import TestBase
from json import loads
from unittest import skip
from parameterized import parameterized


class TestPartialUpdateBooking(TestBase):
    """
    Class for testing partial update of bookings
    """
    base = TestBase()

    @classmethod
    def setUpClass(cls):
        """
        Authenticate admin user; create booking.
        """
        cls.base.create_token()
        booking_data = cls.base.create_booking().json()
        cls.booking = booking_data["booking"]
        cls.booking_id = booking_data["bookingid"]

    def test_partial_update_booking_success(self):
        """
        Test successful partial update of existent booking
        """
        full_name = {"firstname": "Dervent", "lastname": "Weatherly"}
        response = self.base.partial_update_booking(self.booking_id, full_name)

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())

        # Verify that intended fields are updated
        self.assertEqual(full_name["firstname"], response.json()["firstname"])
        self.assertEqual(full_name["lastname"], response.json()["lastname"])

        # Verify no other fields are updated
        self.assertTrue(self.is_dict_identical(self.booking, response.json(), ["firstname", "lastname"]))

    def test_partial_update_booking_empty_json_success(self):
        """
        Test no partial update occurs when empty JSON object is provided
        """
        original_json = self.get_booking(self.booking_id).json()
        response = self.base.partial_update_booking(self.booking_id, {})

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())
        self.assertTrue(self.is_dict_identical(original_json, response.json()))

    @parameterized.expand([
        # Empty string for name
        '{"firstname": "", "lastname": ""}',

        # Negative total price
        '{"totalprice": -100}',

        # Booking dates in the past
        '{"bookingdates": {"checkin": "2000-01-01", "checkout": "2000-01-02"}}'
    ])
    @skip("Bug: API does not properly handle requests with negative values.")
    def test_partial_update_booking_failure(self, data):
        """
        Test failed partial update when invalid values are provided
        """
        response = self.partial_update_booking(self.booking_id, loads(data))

        # Verify that booking failed to be created
        self.assertEqual(400, response.status_code)
        self.assertEqual("Bad Request", response.text)

    @skip("Bug: API does not properly handle requests with nonexistent booking IDs.")
    def test_partial_update_booking_nonexistent_failure(self):
        """
        Test failed partial update when nonexistent ID is provided
        """
        response = self.base.partial_update_booking("invalidID", {})

        self.assertEqual(404, response.status_code)
        self.assertEqual("Not Found", response.text)
