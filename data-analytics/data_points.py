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

        number = 30
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
                            self.suburb_grid[suburb].append((lat, lon))
                        else:
                            self.suburb_grid[suburb] = [(lat, lon)]

        with open("../src/data/suburb_grid.data", 'w') as grid_file:
            for suburb in self.suburb_grid:
                grid_file.write(suburb + ", " + str(self.suburb_grid[suburb]) + "\n")


    def execute(self):
        self.load_data()
        self.generate_suburb_grid()

if __name__ == '__main__':
    dp = DataPoints()
    dp.execute()