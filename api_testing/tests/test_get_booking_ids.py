from api_testing.resources.test_base import TestBase
from json import loads
from uuid import uuid4
from parameterized import parameterized


class TestGetBookingIDs(TestBase):
    """
    Class for testing the retrieval of booking IDs
    """

    first_name = "Dervent"
    last_name = "Weatherly"
    uuid = uuid4().hex

    @classmethod
    def setUpClass(cls):
        """
        Create two separate bookings with same data.
        """
        data = {"firstname": f"{cls.first_name}", "lastname": f"{cls.last_name}"}
        base = TestBase()
        base.create_booking(data)
        base.create_booking(data)

    @parameterized.expand([
        f'{{"firstname": "{first_name}"}}',
        f'{{"lastname": "{last_name}"}}',
        f'{{"firstname": "{first_name}", "lastname": "{last_name}"}}'
    ])
    def test_get_booking_ids_by_name_success(self, parameters):
        """
        Test success getting booking IDs using valid values for first & last name
        """
        response = self.get_booking_ids(loads(parameters))

        self.assertEqual(200, response.status_code)
        self.assertGreaterEqual(len(response.json()), 2)
        for member in response.json():
            self.assertIsNotNone(member["bookingid"])

    @parameterized.expand([
        # Empty string for first name
        '{"firstname": ""}',

        # Random UUID for last name
        f'{{"lastname": "{last_name}-{uuid}"}}',

        # Random UUID for first name and empty string for last name
        f'{{"firstname": "{first_name}-{uuid}", "lastname": ""}}'
    ])
    def test_get_booking_ids_by_name_failure(self, parameters):
        """
        Test failure getting booking IDs using invalid values for first & last name
        """
        response = self.get_booking_ids(loads(parameters))

        self.assertEqual(200, response.status_code)
        self.assertFalse(response.json())
