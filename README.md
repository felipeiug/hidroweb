# phydro

Biblioteca Python para consultar endpoints do Hidroweb.

## Instalacao

Instale localmente em modo editavel:

```bash
pip install -e .
```

Instale direto do GitHub:

```bash
pip install "git+https://github.com/felipeiug/phydro.git"
```

## Uso

```python
from phydro import download_document, get_stations_list

stations = get_stations_list()
inventory_zip = download_document(document_id=396)
```

`get_stations_list()` retorna um `GeoDataFrame` em `EPSG:4326`.

## API publica

- `phydro.get_stations_list`
- `phydro.download_document`
- `phydro.generate_token`
- `phydro.get_headers`
