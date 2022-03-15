"""
Fixtures for API tests.
"""
from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
from random import randint
import pytest
import requests


@pytest.fixture(scope="session")
def token() -> None:
    """
    Gets auth token for admin user.
    """
    request_header = {"Content-Type": "application/json"}
    request_data = {
        "username": const.USERNAME,
        "password": const.PASSWORD
    }
    response = requests.post(f"{const.HOST}{const.AUTH_ENDPOINT}",
                             headers=request_header, json=request_data)
    return response.json()["token"]


@pytest.fixture
def booking(token) -> dict:
    """
    Creates booking object in API
    """
    booking_dict = const.VALID_BOOKING.copy()
    booking = base.post(booking_dict).json()
    yield booking
    base.delete(booking["bookingid"], token)


@pytest.fixture
def partial_booking_dict() -> dict:
    """
    Returns partial booking data
    """
    return {"totalprice": randint(100, 1000)}
