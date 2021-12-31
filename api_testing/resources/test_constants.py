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

CONFIG = configparser.ConfigParser()
CONFIG.read(DATA_FILE)

HOST = CONFIG.get(TEST_ENVIRONMENT, "host")

# Endpoints
BOOKING_ENDPOINT = "/booking"
