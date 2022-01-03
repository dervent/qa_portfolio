from api_testing.resources.test_base import TestBase


class TestGetBooking(TestBase):
    """
    Class for testing getting bookings by ID
    """

    def test_get_booking_success(self):
        """
        Test successfully getting a single booking by ID
        """
        # Create new booking and store its ID
        booking_id = self.create_booking().json()["bookingid"]
        response = self.get_booking(booking_id)

        # Verify that the correct booking is retrieved
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())
        self.assertTrue(self.is_dict_identical(self.request_json, response.json()))

    def test_get_booking_failure(self):
        """
        Test failure getting booking with nonexistent ID
        """
        response = self.get_booking("invalidID")

        self.assertEqual(404, response.status_code)
        self.assertEqual("Not Found", response.text)
