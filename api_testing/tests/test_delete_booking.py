from api_testing.resources.test_base import TestBase
from unittest import skip


class TestDeleteBooking(TestBase):
    """
    Class for testing the deletion of bookings
    """
    base = TestBase()
    booking_id = None

    @classmethod
    def setUpClass(cls):
        """
        Authenticate user.
        Create booking and assign its data.
        """
        cls.base.create_token()
        cls.booking_id = cls.base.create_booking().json()["bookingid"]

    def test_delete_booking_success(self):
        """
        Test successfully deleting an existing booking
        """
        # Use object 'base', which has token variable set, to make API call
        response = self.base.delete_booking(self.booking_id)

        self.assertEqual(201, response.status_code)
        self.assertEqual("Created", response.text)

        # Verify that booking can no longer be found
        response = self.base.get_booking(self.booking_id)

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
