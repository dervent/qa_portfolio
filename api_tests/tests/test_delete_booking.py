"""
Tests for deletion of bookings
"""
from api_tests.base import test_base as base
from api_tests.tests import SKIP_REASON, INVALID_ID
import pytest


def test_delete_booking_success(admin_token, valid_booking_data) -> None:
    """
    Test success deleting an existing booking
    """
    # Create booking
    response = base.post(valid_booking_data)
    assert response.status_code == 200 and response.json()
    booking_id = response.json()["bookingid"]

    # Make request to delete booking
    response = base.delete(booking_id, admin_token)
    assert response.status_code == 201

    # Verify that booking cannot be retrieved
    response = base.get(booking_id=booking_id)
    assert response.status_code == 404
    assert response.text == "Not Found"


@pytest.mark.skip(reason=SKIP_REASON)
def test_delete_booking_failure(admin_token) -> None:
    """
    Test failure to delete a nonexistent booking
    """
    response = base.delete(INVALID_ID, admin_token)
    assert response.status_code == 404
    assert response.text == "Not Found"


def test_delete_booking_failure_forbidden() -> None:
    """
    Test failure to delete a booking without authorization
    """
    response = base.delete(INVALID_ID)
    assert response.status_code == 403
    assert response.text == "Forbidden"
