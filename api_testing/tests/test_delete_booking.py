from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
import pytest


def test_delete_booking_success(booking: dict, token: str) -> None:
    """
    Test successfully deleting an existing booking
    """
    booking_id = booking["bookingid"]

    # Make request to delete booking
    response = base.delete(booking_id, token)
    assert response.status_code == 201

    # Verify that booking cannot be retrieved
    response = base.get_booking(booking_id)
    assert response.status_code == 404
    assert response.text == "Not Found"


@pytest.mark.skip(reason=const.SKIP_REASON)
def test_delete_booking_failure(token: str) -> None:
    """
    Test failure to delete a nonexistent booking
    """
    response = base.delete(const.INVALID_ID, token)
    assert response.status_code == 404
    assert response.text == "Not Found"


def test_delete_booking_failure_forbidden() -> None:
    """
    Test failure to delete a booking without authorization
    """
    response = base.delete(const.INVALID_ID)
    assert response.status_code == 403
    assert response.text == "Forbidden"
