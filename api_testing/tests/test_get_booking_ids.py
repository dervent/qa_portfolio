"""
Tests for retrieval of booking IDs
"""
from api_testing.base import test_base as base
from api_testing.api_objects.booking import Booking, BookingDates
from datetime import date, timedelta
import uuid
import pytest

RAND_HEX = uuid.uuid4().hex
name = {"firstname": f"Hello-{RAND_HEX}", "lastname": f"World-{RAND_HEX}"}


@pytest.fixture(autouse=True, scope="module")
def manage_bookings(admin_token) -> None:
    """
    Manage two valid bookings
    """
    week_from_now = date.today() + timedelta(days=7)
    booking_dates = BookingDates(week_from_now, week_from_now + timedelta(days=7))
    booking_obj = Booking(name["firstname"], name["lastname"], 1000.25, True, booking_dates, "Breakfast")

    # Create bookings
    ids = set()
    for i in range(2):
        response = base.post(booking_obj.get_dict())
        assert response.status_code == 200 and "bookingid" in response.json(), "Failed to create booking."
        ids.add(response.json()["bookingid"])

    yield

    # Delete all previously created bookings
    for booking_id in ids:
        response = base.delete(booking_id, admin_token)
        assert response.status_code == 201, f"Failed to delete booking with ID: {booking_id}"


@pytest.mark.parametrize("parameters", [
    {"firstname": name["firstname"]},
    {"lastname": name["lastname"]},
    {"firstname": name["firstname"], "lastname": name["lastname"]}
])
def test_get_booking_ids_success(parameters) -> None:
    """
    Test success getting booking IDs using valid values for first & last name
    """
    response = base.get(request_params=parameters)
    assert 200 == response.status_code
    assert len(response.json()) == 2
    for member in response.json():
        assert "bookingid" in member.keys()


@pytest.mark.parametrize("parameters", [
    {"firstname": ""},
    {"lastname": RAND_HEX},
    {"firstname": RAND_HEX, "lastname": ""}
])
def test_get_booking_ids_failure(parameters) -> None:
    """
    Test failure getting booking IDs using nonexistent values for first & last name
    """
    response = base.get(request_params=parameters)
    assert 200 == response.status_code
    assert not response.json()


def test_get_all_booking_ids() -> None:
    """
    Test success getting all known booking IDs when no query parameters are specified
    """
    response = base.get()
    assert 200 == response.status_code
    assert len(response.json()) >= 2
