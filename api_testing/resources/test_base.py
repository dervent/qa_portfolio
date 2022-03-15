from api_testing.resources import test_constants as const
from deepdiff import DeepDiff
import requests


url: str = f"{const.HOST}{const.BOOKING_ENDPOINT}"


def post(data: dict = None) -> requests.Response:
    """
    Make a request to create a new booking.
    :param data: data in request body
    :return: Response object
    """
    request_header = {"Content-Type": "application/json"}
    return requests.post(url, headers=request_header, json=data)


def get_booking_ids(request_params: dict = None) -> requests.Response:
    """
    Make a request to get all booking IDs.
    :param request_params: query parameter key-values
    :return: Response object
    """
    return requests.get(url, params=request_params)


def get_booking(booking_id: str) -> requests.Response:
    """
    Make a request to get a specific booking.
    :param booking_id: booking ID
    :return: Response object
    """
    return requests.get(f"{url}/{booking_id}")


def put(booking_id: str, request_data: dict = None, token: str = None) -> requests.Response:
    """
    Make a request to update a current booking.
    :param booking_id: booking ID
    :param request_data: data in request body
    :param token: authorization token
    :return: Response object
    """
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if token:
        request_headers.update({"Cookie": f"token={token}"})
    return requests.put(f"{url}/{booking_id}", headers=request_headers, json=request_data)


def patch(booking_id: str, request_data: dict = None, token: str = None) -> requests.Response:
    """
    Make a request to update a current booking with partial data.
    :param booking_id: booking ID
    :param request_data: partial data to update booking with
    :param token: authorization token
    :return: Response object
    """
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if token:
        request_headers.update({"Cookie": f"token={token}"})
    return requests.patch(f"{url}/{booking_id}", headers=request_headers, json=request_data)


def delete(booking_id: str, token: str = None) -> requests.Response:
    """
    Make a request to delete a current booking.
    :param booking_id: booking ID
    :param token: authorization token
    :return: Response object
    """
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if token:
        request_headers.update({"Cookie": f"token={token}"})
    return requests.delete(f"{url}/{booking_id}", headers=request_headers)


def is_dict_identical(actual_dict: dict, expected_dict: dict, exclude_keys: list = None) -> bool:
    """
    Returns whether or not actual and expected dict objects match
    :param actual_dict: actual dict
    :param expected_dict: expected dict
    :param exclude_keys: list of keys to ignore when comparing dicts
    :return: true if both dicts match; false otherwise
    """
    exclude_paths = []

    if exclude_keys:
        for key in exclude_keys:
            path = "root"
            for json_ele in key.split("/"):
                path += f"['{json_ele}']"
            exclude_paths.append(path)

    dict_difference = DeepDiff(expected_dict, actual_dict, ignore_order=True, exclude_paths=exclude_paths)

    if bool(dict_difference) is True:
        return False

    return True
