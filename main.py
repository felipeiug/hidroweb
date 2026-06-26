from hidroweb import download_document, get_stations_list


def main() -> None:
    stations = get_stations_list()
    stations.to_file("teste.shp")

    inventory_zip = download_document(document_id=396)
    print(stations)
    print(inventory_zip)


if __name__ == "__main__":
    main()
