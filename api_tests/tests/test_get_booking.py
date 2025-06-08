"""
Tests for retrieval of bookings
"""
from api_tests.base import test_base as base
from api_tests.tests import INVALID_ID


def test_get_booking_success(valid_booking) -> None:
    """
    Test success getting a single booking by ID
    """
    response = base.get(booking_id=valid_booking["bookingid"])

    # Verify that the correct booking is retrieved
    assert response.status_code == 200
    assert response.json()
    assert base.is_dict_identical(response.json(), valid_booking["booking"])


def test_get_booking_failure() -> None:
    """
    Test failure getting booking with nonexistent ID
    """
    response = base.get(booking_id=INVALID_ID)
    assert response.status_code == 404
    assert response.text == "Not Found"
