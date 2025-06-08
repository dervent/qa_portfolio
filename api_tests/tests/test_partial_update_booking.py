"""
Tests for partially updating bookings
"""
from api_tests.tests import SKIP_REASON, INVALID_ID
from api_tests.base import test_base as base
from api_tests.api_objects.booking import Booking
from random import randint
import pytest


def test_partial_update_booking_success(valid_booking, admin_token) -> None:
    """
    Test successful partial update of existent booking
    """
    partial_booking = Booking(totalprice=randint(100, 1000)).get_dict()
    booking_id = valid_booking["bookingid"]

    # Update booking with partial data
    response = base.patch(booking_id, partial_booking, admin_token)
    assert response.status_code == 200
    assert response.json()

    # Retrieve booking and verify partial update
    response = base.get(booking_id)
    assert response.status_code == 200
    assert response.json()
    for key in partial_booking:
        assert response.json()[key] == partial_booking[key]

    # Verify no other fields are updated
    assert base.is_dict_identical(response.json(), valid_booking["booking"], list(partial_booking.keys()))


def test_partial_update_booking_success_empty_object(valid_booking, admin_token) -> None:
    """
    Test no partial update occurs when empty JSON object is provided
    """
    booking_id = valid_booking["bookingid"]

    response = base.patch(booking_id, {}, admin_token)
    assert response.status_code == 200
    assert response.json()

    response = base.get(booking_id)
    assert response.status_code == 200
    assert base.is_dict_identical(response.json(), valid_booking["booking"])


@pytest.mark.skip(reason=SKIP_REASON)
def test_partial_update_booking_failure_invalid_id(admin_token) -> None:
    """
    Test failed partial update when nonexistent ID is provided
    """
    response = base.patch(INVALID_ID, {}, admin_token)
    assert response.status_code == 404
    assert response.text == "Not Found"


def test_partial_update_booking_failure_forbidden() -> None:
    """
    Test failure to partially update a booking without authorization
    """
    response = base.patch(INVALID_ID, {})
    assert response.status_code == 403
    assert response.text == "Forbidden"
