from api_testing import API_HOST
from deepdiff import DeepDiff
import requests


def get(booking_id: str = None, request_params: dict = None) -> requests.Response:
    """
    Make a request to get all booking IDs or a specific booking.
    :param booking_id: booking ID
    :param request_params: query parameter key-values
    """
    request_url = (f"{API_HOST}/booking/{booking_id}", f"{API_HOST}/booking")[booking_id is None]
    return requests.get(request_url, params=request_params)


def put(booking_id: str, request_data: dict = None, token: str = None) -> requests.Response:
    """
    Make a request to update a current booking.
    :param booking_id: booking ID
    :param request_data: api_objects in request body
    :param token: authorization token
    :return: Response object
    """
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if token:
        request_headers.update({"Cookie": f"token={token}"})
    return requests.put(f"{API_HOST}/booking/{booking_id}", headers=request_headers, json=request_data)


def post(data: dict = None) -> requests.Response:
    """
    Make a request to create a new booking.
    :param data: api_objects in request body
    :return: Response object
    """
    request_header = {"Content-Type": "application/json", "Accept": "application/json"}
    return requests.post(f"{API_HOST}/booking", headers=request_header, json=data)


def patch(booking_id: str, request_data: dict = None, token: str = None) -> requests.Response:
    """
    Make a request to update a current booking with partial api_objects.
    :param booking_id: booking ID
    :param request_data: partial api_objects to update booking with
    :param token: authorization token
    :return: Response object
    """
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if token:
        request_headers.update({"Cookie": f"token={token}"})
    return requests.patch(f"{API_HOST}/booking/{booking_id}", headers=request_headers, json=request_data)


def delete(booking_id: str, token: str = None) -> requests.Response:
    """
    Make a request to delete a current booking.
    :param booking_id: booking ID
    :param token: authorization token
    :return: Response object
    """
    # import pdb; pdb.set_trace()
    request_headers = {"Content-Type": "application/json"}
    if token:
        request_headers.update({"Cookie": f"token={token}"})
    return requests.delete(f"{API_HOST}/booking/{booking_id}", headers=request_headers)


def is_dict_identical(actual_dict: dict, expected_dict: dict, exclude_keys: list = None) -> bool:
    """
    Returns whether actual and expected dict objects match
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
