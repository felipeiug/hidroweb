from phydro import get_stations_list, get_station_data


def main() -> None:
    # stations = get_stations_list()
    # stations.to_file("teste.shp")

    station_data = get_station_data(48000)
    print(station_data)

if __name__ == "__main__":
    main()
