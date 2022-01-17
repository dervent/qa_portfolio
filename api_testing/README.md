# API Tests
This API test suite covers cases for the [Restful-Booker API](https://restful-booker.herokuapp.com/).
To run the tests, this readme assumes you have Python 3.8 installed on a Linux or MacOS machine.

## Running Tests
Create and activate a virtual environment:
```shell
python3 -m venv name-of-venv
source name-of-venv/bin/activate
```

Install dependencies: <br/>
`pip3 install -r requirements.pip`

Set environment variables for admin credentials. Values can be obtained from the Restful-Booker
API documentation [here](https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth-CreateToken).
```shell
export export USERNAME=value
export export PASSWORD=value
```

Run test suite (optionally with verbose flag): <br/>
`pytest --verbose tests/`
