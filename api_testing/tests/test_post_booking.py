from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
import pytest


def test_post_booking_success() -> None:
    """
    Test POST booking success
    """
    booking = const.VALID_BOOKING.copy()

    # Create booking and verify presence of ID in response
    response = base.post(booking)
    assert response.status_code == 200
    assert "bookingid" in response.json().keys()

    # Retrieve booking to verify all values in response
    booking_id = response.json()["bookingid"]
    response = base.get_booking(booking_id)
    assert response.status_code == 200
    assert response.json() is not None
    assert base.is_dict_identical(response.json(), booking)


@pytest.mark.skip(reason=const.SKIP_REASON)
@pytest.mark.parametrize("invalid_data", const.INVALID_BOOKINGS)
def test_post_booking_failure(invalid_data: dict) -> None:
    """
    Test POST booking failure
    """
    # Replace corresponding values in booking object with invalid data
    booking = const.VALID_BOOKING.copy()
    for key in invalid_data:
        booking[key] = invalid_data[key]

    # Attempt to create booking with invalid values
    response = base.post(booking)
    assert response.status_code == 400
    assert response.status_code == "Bad Request"
