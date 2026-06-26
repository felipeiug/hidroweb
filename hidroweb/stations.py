from __future__ import annotations

from math import isfinite

import geopandas as gpd
import pandas as pd
import requests
from shapely import Point
from tqdm.auto import trange

from hidroweb.auth import get_headers

STATIONS_URL = "https://www.snirh.gov.br/hidroweb/rest/api/dadosHistoricos?size={size}&page={page}"


def _is_finite_number(value: object) -> bool:
    return pd.notna(value) and isfinite(float(value))


def _build_point(longitude: object, latitude: object, altitude: object) -> Point | None:
    if not _is_finite_number(longitude) or not _is_finite_number(latitude):
        return None

    longitude = float(longitude)
    latitude = float(latitude)

    if _is_finite_number(altitude):
        return Point(longitude, latitude, float(altitude))

    return Point(longitude, latitude)


def get_stations_list(
    page_size: int = 1000,
    show_progress: bool = True,
    timeout: int = 60,
) -> gpd.GeoDataFrame:
    """Fetch Hidroweb stations as a GeoDataFrame."""
    stations: list[dict] = []

    resp = requests.get(
        STATIONS_URL.format(size=page_size, page=0),
        headers=get_headers(),
        timeout=timeout,
    )
    resp.raise_for_status()
    data = resp.json()

    stations.extend(data.get("content", []))
    total_pages = data.get("totalPages", 0)

    pages = range(1, total_pages)
    if show_progress:
        pages = trange(1, total_pages, desc="Obtendo estacoes", total=max(total_pages - 1, 0))

    for page in pages:
        resp = requests.get(
            STATIONS_URL.format(size=page_size, page=page),
            headers=get_headers(),
            timeout=timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        stations.extend(data.get("content", []))

    stations_df = pd.DataFrame(stations)
    geometry = [
        _build_point(longitude, latitude, altitude)
        for longitude, latitude, altitude in zip(
            stations_df["longitude"],
            stations_df["latitude"],
            stations_df["altitude"],
        )
    ]

    return gpd.GeoDataFrame(stations_df, geometry=geometry, crs="EPSG:4326")
