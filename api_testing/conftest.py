"""
Fixtures for test suite
"""
from api_testing import API_HOST
from api_testing.api_objects.booking import Booking, BookingDates
from datetime import date, timedelta
import os
import pytest
import requests


@pytest.fixture(scope="session")
def admin_token() -> None:
    """
    Get auth token for admin user.
    """
    # Ensure environment variables are set.
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    if username is None or password is None:
        raise EnvironmentError("Must set USERNAME and PASSWORD env vars.")

    # Make request to get admin token, and return value to caller.
    request_header = {"Content-Type": "application/json"}
    request_data = {"username": username, "password": password}
    response = requests.post(f"{API_HOST}/auth", headers=request_header, json=request_data)
    assert (response.status_code == 200 and
            response.json() and
            response.json()["token"]), "Failed to get admin token."
    return response.json()["token"]


@pytest.fixture()
def valid_booking_data() -> dict:
    """
    Create and return Booking data as dict object.
    """
    week_from_now = date.today() + timedelta(days=7)
    booking_dates = BookingDates(week_from_now, week_from_now + timedelta(days=7))
    booking_obj = Booking("Dervent", "West", 1000, True, booking_dates, "Breakfast")
    return booking_obj.get_dict()


@pytest.fixture
def valid_booking(admin_token, valid_booking_data) -> dict:
    """
    Create a standard booking object in API.
    """
    # Create booking and return response JSON.
    request_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(f"{API_HOST}/booking", headers=request_headers, json=valid_booking_data)
    assert response.status_code == 200 and "bookingid" in response.json(), "Failed to create booking."

    yield response.json()

    # Delete booking from API.
    booking_id = response.json()["bookingid"]
    request_headers = {"Content-Type": "application/json", "Cookie": f"token={admin_token}"}
    response = requests.delete(f"{API_HOST}/booking/{booking_id}", headers=request_headers)
    assert response.status_code == 201, f"Failed to delete booking with ID: {booking_id}"
