# API Tests
This API test suite covers cases for the [Restful-Booker API](https://restful-booker.herokuapp.com/).

## Running Tests
1. Use Python 3.12 or later. 
2. Create and activate a new virtual environment.
3. Install test requirements while in the root directory: `pip3 install -r api_testing/test-requirements.pip`
4. Ensure you have the below env vars set. The value for each can be retrieved from the Restful-Booker API [documentation](https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth-CreateToken).
    * `USERNAME`
    * `PASSWORD`
5. Run the API test suite (optionally with verbose flag): `pytest --verbose api_testing/tests/`
