from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
from uuid import uuid4
import pytest

name = {"firstname": "Hello", "lastname": "World"}
uuid: str = uuid4().hex


def setup_module() -> None:
    """
    Create two separate bookings
    """
    booking = const.VALID_BOOKING.copy()
    booking.update(name)
    base.post(booking)
    base.post(booking)


@pytest.mark.parametrize("parameters", [
    {"firstname": name["firstname"]},
    {"lastname": name["lastname"]},
    {"firstname": name["firstname"], "lastname": name["lastname"]}
])
def test_get_booking_ids_success(parameters: dict) -> None:
    """
    Test success getting booking IDs using valid values for first & last name
    """
    response = base.get_booking_ids(parameters)
    assert 200 == response.status_code
    assert len(response.json()) >= 2
    for member in response.json():
        assert "bookingid" in member.keys()


@pytest.mark.parametrize("parameters", [
    {"firstname": ""},
    {"lastname": f"{uuid}"},
    {"firstname": f"{uuid}", "lastname": ""}
])
def test_get_booking_ids_failure(parameters: dict) -> None:
    """
    Test failure getting booking IDs using nonexistent values for first & last name
    """
    response = base.get_booking_ids(parameters)
    assert 200 == response.status_code
    assert not response.json()


def test_get_all_booking_ids() -> None:
    """
    Test success getting all known booking IDs when no query parameters are specified
    """
    response = base.get_booking_ids()
    assert 200 == response.status_code
    assert len(response.json()) >= 2
