from api_testing.base import test_base as base


def test_post_booking_success(valid_booking_data) -> None:
    """
    Test success creating booking
    """
    # Create booking and verify presence of ID in response
    response = base.post(valid_booking_data)
    assert response.status_code == 200
    assert response.json() and "bookingid" in response.json()

    # Retrieve booking to verify all values in response
    booking_id = response.json()["bookingid"]
    response = base.get(booking_id)
    assert response.status_code == 200
    assert response.json() is not None
    assert base.is_dict_identical(response.json(), valid_booking_data)
