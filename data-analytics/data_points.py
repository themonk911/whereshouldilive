import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class DataPoints:
    def __init__(self):
        self.suburb_polygons = dict()
        self.suburb_grid = dict()

        self.min_lat = float(sys.maxint)
        self.min_lon = float(sys.maxint)
        self.max_lat = float(-sys.maxint)
        self.max_lon = float(-sys.maxint)

    def load_data(self):
        file_name = "../datasets/ACT_Division_Boundaries_data.csv"
        with open(file_name, 'r') as file:
            for index, line in enumerate(file.readlines()):
                if index == 0:
                    continue

                coordinates_shapely = []
                line = line.strip()
                coordinates = line[line.find("(((")+3:line.find(")))")].split(',')
                for coordinate in coordinates:
                    split_line = coordinate.strip().split(' ')

                    lon = float(split_line[0])
                    lat = float(split_line[1])
                    # print(lon, lat)
                    coordinates_shapely.append(
                        (
                            lon,
                            lat
                        )
                    )

                if lon > self.max_lon:
                    self.max_lon = lon
                if lon < self.min_lon:
                    self.min_lon = lon
                if lat > self.max_lat:
                    self.max_lat = lat
                if lat < self.min_lat:
                    self.min_lat = lat

                split_line = line.split(',')
                suburb = split_line[len(split_line)-4]

                self.suburb_polygons[suburb] = coordinates_shapely

    def generate_suburb_grid(self):
        diff_lon = self.max_lon - self.min_lon
        diff_lat = self.max_lat - self.min_lat

        number = 50
        delta_lon = diff_lon / float(number)
        delta_lat = diff_lat / float(number)

        for index_lon in range(number):
            for index_lat in range(number):
                lon = self.min_lon + delta_lon * float(index_lon)
                lat = self.min_lat + delta_lat * float(index_lat)

                point = Point(lon, lat)

                for suburb in self.suburb_polygons:
                    # print suburb, len(self.suburb_polygons[suburb])
                    if Polygon(self.suburb_polygons[suburb]).contains(point):
                        print suburb, point
                        if suburb in self.suburb_grid:
                            self.suburb_grid[suburb].append((lon, lat))
                        else:
                            self.suburb_grid[suburb] = [(lon, lat)]

        with open("../src/data/suburb_grid.data", 'w') as grid_file:
            for suburb in self.suburb_grid:
                grid_file.write(suburb + ", " + str(self.suburb_grid[suburb]) + "\n")

    def get_number_of_bus_stops_per_suburb(self, array_of_bus_stops):
        bus_stops_per_suburb = dict()

        for bus_stop in array_of_bus_stops:
            for suburb in self.suburb_polygons:
                # print bus_stop
                try:
                    point = Point(float(bus_stop[0]), float(bus_stop[1]))
                except:
                    continue

                if Polygon(self.suburb_polygons[suburb]).contains(point):
                    # print suburb, point
                    if suburb in bus_stops_per_suburb:
                        bus_stops_per_suburb[suburb] = bus_stops_per_suburb[suburb] + 1
                        # self.bus_stops_per_suburb[suburb].append([bus_stop[0], bus_stop[1]])
                    else:
                        bus_stops_per_suburb[suburb] = 1
                        # self.bus_stops_per_suburb[suburb] = [[bus_stop[0], bus_stop[1]]]

        return bus_stops_per_suburb


    def execute(self):
        self.load_data()
        self.generate_suburb_grid()

if __name__ == '__main__':
    dp = DataPoints()
    dp.execute()