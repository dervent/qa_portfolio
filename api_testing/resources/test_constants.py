"""
Constants used across classes
"""
import configparser
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
DATA_FILE = os.path.join(DATA_DIR, "data.ini")
if not os.path.exists(DATA_FILE):
    raise OSError(f"{DATA_FILE} does not exist.")

TEST_ENVIRONMENT = os.environ.get("TEST_ENVIRONMENT", "production")

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
if USERNAME is None or PASSWORD is None:
    raise ValueError("Must set USERNAME and PASSWORD variables for access to API.")

CONFIG = configparser.ConfigParser()
CONFIG.read(DATA_FILE)

HOST = CONFIG.get(TEST_ENVIRONMENT, "host")

# Endpoints
AUTH_ENDPOINT = "/auth"
BOOKING_ENDPOINT = "/booking"
