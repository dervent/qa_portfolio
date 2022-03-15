from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
import pytest


def test_put_booking_success(booking: dict, partial_booking_dict: dict, token: str) -> None:
    """
    Test successful update of existent booking
    """
    booking_id = booking["bookingid"]
    new_booking = booking["booking"].copy()
    new_booking.update(partial_booking_dict)

    response = base.put(booking_id, new_booking, token)
    assert response.status_code == 200
    assert response.json()

    response = base.get_booking(booking_id)
    assert response.status_code == 200
    assert not base.is_dict_identical(response.json(), booking["booking"])
    assert base.is_dict_identical(response.json(), new_booking)


def test_put_booking_failure_partial_data(booking: dict, partial_booking_dict: dict, token: str) -> None:
    """
    Test failure to update existent booking with partial data
    """
    response = base.put(booking["bookingid"], partial_booking_dict, token)
    assert response.status_code == 400
    assert response.text == "Bad Request"


@pytest.mark.skip(reason=const.SKIP_REASON)
def test_put_booking_failure_invalid_id(token: str) -> None:
    """
    Test failure to update a nonexistent booking
    """
    response = base.put(const.INVALID_ID, {}, token)
    assert response.status_code == 404
    assert response.text == "Not Found"


def test_put_booking_failure_forbidden() -> None:
    """
    Test failure to update a booking without authorization
    """
    response = base.put(const.INVALID_ID, {})
    assert response.status_code == 403
    assert response.text == "Forbidden"
