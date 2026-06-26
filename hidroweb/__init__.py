"""Python client for selected Hidroweb endpoints."""

from hidroweb.auth import generate_token, get_headers
from hidroweb.station_data import download_document
from hidroweb.stations import get_stations_list

__all__ = [
    "download_document",
    "generate_token",
    "get_headers",
    "get_stations_list",
]

__version__ = "0.1.0"
