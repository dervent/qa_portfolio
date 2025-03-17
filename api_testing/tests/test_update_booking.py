from api_testing.base import test_base as base
from api_testing.tests import SKIP_REASON, INVALID_ID
from api_testing.api_objects.booking import Booking
import pytest

partial_booking = Booking(totalprice=300, additionalneeds="crib").get_dict()

def test_put_booking_success(valid_booking, admin_token) -> None:
    """
    Test successful update of existent booking
    """
    booking_id = valid_booking["bookingid"]
    new_booking = valid_booking["booking"].copy()
    new_booking.update(partial_booking)

    response = base.put(booking_id, new_booking, admin_token)
    assert response.status_code == 200
    assert response.json()

    response = base.get(booking_id)
    assert response.status_code == 200
    assert not base.is_dict_identical(response.json(), valid_booking["booking"])
    assert base.is_dict_identical(response.json(), new_booking)


def test_put_booking_failure_partial_data(valid_booking, admin_token) -> None:
    """
    Test failure to update existent booking with partial api_objects
    """
    response = base.put(valid_booking["bookingid"], partial_booking, admin_token)
    assert response.status_code == 400
    assert response.text == "Bad Request"


@pytest.mark.skip(reason=SKIP_REASON)
def test_put_booking_failure_invalid_id(admin_token) -> None:
    """
    Test failure to update a nonexistent booking
    """
    response = base.put(INVALID_ID, {}, admin_token)
    assert response.status_code == 404
    assert response.text == "Not Found"


def test_put_booking_failure_forbidden() -> None:
    """
    Test failure to update a booking without authorization
    """
    response = base.put(INVALID_ID, {})
    assert response.status_code == 403
    assert response.text == "Forbidden"
