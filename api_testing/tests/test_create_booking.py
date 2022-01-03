from api_testing.resources.test_base import TestBase
from unittest import skip
from json import loads
from parameterized import parameterized


class TestCreateBooking(TestBase):
    """
    Class for testing the creation of bookings
    """

    def test_create_booking_success(self):
        """
        Test create booking success
        """
        # Create booking with default, valid values
        response = self.create_booking()

        # Verify booking is created successfully and correctly
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())
        self.assertIsInstance(response.json()["bookingid"], int)
        self.assertTrue(self.is_dict_identical(self.request_json, response.json()["booking"]))

    @parameterized.expand([
        # Empty string for name
        '{"firstname": "", "lastname": ""}',
        
        # Negative total price
        '{"totalprice": -100}',

        # Booking dates in the past
        '{"bookingdates": {"checkin": "2000-01-01", "checkout": "2000-01-02"}}'
    ])
    @skip("Bug: API does not properly handle negative cases.")
    def test_create_booking_failure(self, data):
        """
        Test create booking failure
        """
        # Modify booking with invalid values
        response = self.create_booking(loads(data))

        # Verify that booking failed to be created
        self.assertEqual(400, response.status_code)
        self.assertEqual("Bad Request", response.text)
