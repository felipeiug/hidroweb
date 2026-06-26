"""Python client for selected Hidroweb endpoints."""

from phydro.stations import get_stations_list
from phydro.station_data import get_station_data

__all__ = [
    "get_stations_list",
    "get_station_data"
]

__version__ = "0.1.0"
