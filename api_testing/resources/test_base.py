from api_testing.resources import test_constants as const
from unittest import TestCase
from datetime import datetime, timedelta
from random import choice, randint
from deepdiff import DeepDiff
import requests


class TestBase(TestCase):
    """
    Base class which executes API calls and contains
    functions used across multiple test classes
    """

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.request_json = {}

    def create_booking(self, data=None):
        """
        Creates a new booking
        :param data: booking data to include in request JSON
        :return: Response object
        """
        request_header = {"Content-Type": "application/json"}

        # Create a valid dict object with all fields for booking.
        booking_dates = self.get_dates(7, 7)
        self.request_json = {
            "firstname": "FirstName",
            "lastname": "LastName",
            "totalprice": randint(100, 1000),
            "depositpaid": choice([True, False]),
            "bookingdates": {
                "checkin": booking_dates["checkIn"],
                "checkout": booking_dates["checkOut"]
            },
            "additionalneeds": "Breakfast"
        }

        # If data is provided, replace matching values in above dict object
        if data:
            if not isinstance(data, dict):
                raise TypeError("Parameter request_data must be of type dict.")
            for key in data:
                if key in self.request_json.keys():
                    self.request_json[key] = data[key]

        return requests.post(const.HOST + const.BOOKING_ENDPOINT, headers=request_header, json=self.request_json)

    def get_dates(self, num_days_delta, num_days_stay):
        """
        Returns check-in and check-out days
        :param num_days_delta: number of days to use from current UTC datetime
        :param num_days_stay: duration of stay in number of days
        :return: dict object of check-in and check-out dates
        """
        date_format = "{:%Y-%m-%d}"
        current_utc = datetime.utcnow()
        check_in_date = current_utc + timedelta(days=num_days_delta)
        check_out_date = check_in_date + timedelta(days=num_days_stay)
        return {"checkIn": date_format.format(check_in_date),
                "checkOut": date_format.format(check_out_date)}

    def is_dict_identical(self, expected_dict, actual_dict, exclude_keys=None):
        """
        Returns whether or not expected and actual dict (JSON response body) objects match
        :param expected_dict: object sent as JSON in request
        :param actual_dict: object returned as JSON in response
        :param exclude_keys: list of keys to ignore in JSON object
        :return: true if both objects match; false otherwise
        """
        exclude_paths = []

        if exclude_keys:
            if not isinstance(exclude_keys, list):
                raise TypeError("Parameter exclude_keys must be of type list.")
            for key in exclude_keys:
                path = "root"
                for json_ele in key.split("/"):
                    path += "['%s']" % json_ele
                exclude_paths.append(path)

        dict_difference = DeepDiff(expected_dict, actual_dict, ignore_order=True, exclude_paths=exclude_paths)

        if bool(dict_difference) is True:
            return False

        return True