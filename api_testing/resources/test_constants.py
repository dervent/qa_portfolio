"""
Constants used across classes
"""
import os
import yaml

# Environment variables
USERNAME: str = os.environ.get("USERNAME")
PASSWORD: str = os.environ.get("PASSWORD")
if USERNAME is None or PASSWORD is None:
    raise EnvironmentError("Must set USERNAME and PASSWORD variables.")

# Data file
DATA_DIR: str = os.path.join(os.path.dirname(__file__), "../data")
DATA_FILE: str = os.path.join(DATA_DIR, "booking_objects.yml")
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"{DATA_FILE} does not exist.")
with open(DATA_FILE) as file:
    OBJS: dict = yaml.safe_load(file)
    VALID_BOOKING: dict = OBJS["valid_booking"]
    INVALID_BOOKINGS: list = OBJS["invalid_bookings"]

# Host
HOST: str = "https://restful-booker.herokuapp.com"

# Endpoints
AUTH_ENDPOINT: str = "/auth"
BOOKING_ENDPOINT: str = "/booking"

# Invalid values
INVALID_ID: str = "invalid_id"

# Test skip reason
SKIP_REASON: str = "API does not properly handle such case."
