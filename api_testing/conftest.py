"""
Fixtures for API tests.
"""
from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
from random import randint
import pytest
import requests

TOKEN = None


@pytest.fixture(scope="session", autouse=True)
def set_token():
    """
    Sets value of auth token for admin user.
    """
    request_header = {"Content-Type": "application/json"}
    request_data = {
        "username": const.USERNAME,
        "password": const.PASSWORD
    }
    response = requests.post(f"{const.HOST}{const.AUTH_ENDPOINT}",
                             headers=request_header, json=request_data)
    global TOKEN
    TOKEN = response.json()["token"]


@pytest.fixture
def booking() -> dict:
    """
    Return booking object found in Response body
    :return: booking object
    """
    booking = const.VALID_BOOKING.copy()
    return base.post(booking).json()


@pytest.fixture
def partial_booking_data() -> dict:
    """
    Return partial booking data
    :return: partial booking data
    """
    return {"totalprice": randint(100, 1000)}
