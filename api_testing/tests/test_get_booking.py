from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const


def test_get_booking_success(booking: dict) -> None:
    """
    Test successfully getting a single booking by ID
    """
    response = base.get_booking(booking["bookingid"])

    # Verify that the correct booking is retrieved
    assert response.status_code == 200
    assert response.json()
    assert base.is_dict_identical(response.json(), booking["booking"])


def test_get_booking_failure() -> None:
    """
    Test failure getting booking with nonexistent ID
    """
    response = base.get_booking(const.INVALID_ID)
    assert response.status_code == 404
    assert response.text == "Not Found"
