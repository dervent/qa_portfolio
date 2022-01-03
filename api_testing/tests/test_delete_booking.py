from api_testing.resources.test_base import TestBase
from unittest import skip


class TestDeleteBooking(TestBase):
    """
    Class for testing the deletion of bookings
    """
    base = TestBase()

    @classmethod
    def setUpClass(cls):
        """
        Authenticate admin user.
        """
        cls.base.create_token()

    def test_delete_booking_success(self):
        """
        Test successfully deleting an existing booking
        """
        # Use object 'base', which has token variable set, to make API call
        booking_id = self.base.create_booking().json()["bookingid"]
        response = self.base.delete_booking(booking_id)

        self.assertEqual(201, response.status_code)
        self.assertEqual("Created", response.text)

        # Verify that booking can no longer be found
        response = self.base.get_booking(booking_id)

        self.assertEqual(404, response.status_code)
        self.assertEqual("Not Found", response.text)

    @skip("Bug: API does not properly handle requests with nonexistent booking IDs.")
    def test_delete_booking_failure(self):
        """
        Test failing to delete a nonexistent booking
        """
        response = self.base.delete_booking("nonexistent")

        self.assertEqual(404, response.status_code)
        self.assertEqual("Not Found", response.text)
