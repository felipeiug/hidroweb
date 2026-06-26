import requests
import pandas as pd
import geopandas as gpd
from math import isfinite
from shapely import Point
from tqdm import trange

from estacoesHidroweb.generate_token import get_headers

def get_station_data(cod_estacao:int|str)->gpd.GeoDataFrame:

    url = f'https://www.snirh.gov.br/hidroweb/rest/api/documento/download/files?codigoestacao={cod_estacao}&tipodocumento=txt'

    headers = get_headers()
    resp = requests.get(url, headers=headers)

    resp.raise_for_status()
    dados = resp.json()

    return gpd.GeoDataFrame(estacoes, geometry=points, crs="EPSG:4326")