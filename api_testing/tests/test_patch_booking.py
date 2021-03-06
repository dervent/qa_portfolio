from api_testing.resources import test_base as base
from api_testing.resources import test_constants as const
import pytest


def test_patch_booking_success(booking: dict, partial_booking_dict: dict, token: str) -> None:
    """
    Test successful partial update of existent booking
    """
    booking_id = booking["bookingid"]
    response = base.patch(booking_id, partial_booking_dict, token)
    assert response.status_code == 200
    assert response.json()

    response = base.get_booking(booking_id)
    assert response.status_code == 200
    assert response.json()
    for key in partial_booking_dict:
        assert response.json()[key] == partial_booking_dict[key]

    # Verify no other fields are updated
    assert base.is_dict_identical(response.json(), booking["booking"], list(partial_booking_dict.keys()))


def test_patch_booking_success_empty_object(booking: dict, token: str) -> None:
    """
    Test no partial update occurs when empty JSON object is provided
    """
    booking_id = booking["bookingid"]
    response = base.patch(booking_id, {}, token)
    assert response.status_code == 200
    assert response.json()

    response = base.get_booking(booking_id)
    assert response.status_code == 200
    assert base.is_dict_identical(response.json(), booking["booking"])


# TODO: Research how to call fixtures in parametrized tests
@pytest.mark.skip(reason=const.SKIP_REASON)
@pytest.mark.parametrize("invalid_data", const.INVALID_BOOKINGS)
def test_patch_booking_failure(invalid_data: dict) -> None:
    """
    Test failed partial update when invalid values are provided
    """
    booking_id = base.get_booking_ids().json()[0]["bookingid"]

    response = base.patch(booking_id, invalid_data)
    assert response.status_code == 400
    assert response.text == "Bad Request"


@pytest.mark.skip(reason=const.SKIP_REASON)
def test_patch_booking_failure_invalid_id(token: str) -> None:
    """
    Test failed partial update when nonexistent ID is provided
    """
    response = base.patch(const.INVALID_ID, {}, token)
    assert response.status_code == 404
    assert response.text == "Not Found"


def test_patch_booking_failure_forbidden() -> None:
    """
    Test failure to partially update a booking without authorization
    """
    response = base.patch(const.INVALID_ID, {})
    assert response.status_code == 403
    assert response.text == "Forbidden"
