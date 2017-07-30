from __future__ import print_function
import sys
from geopy.distance import great_circle
import numpy as np

from data_points import DataPoints

class DatasetPreprocessing:
    def __init__(self):
        self.raw_data_folder = "../datasets"
        self.output_folder = "../src/data"

        self.in_act_division_boundaries = "ACT_Division_Boundaries_data.csv"

        self.in_act_police_stations_locations = "ACT_Police_Station_Locations.csv"
        self.in_act_hospital_locations = "Hospitals_in_the_ACT.csv"
        self.in_act_public_toilets = "Public_Toilets_in_the_ACT.csv"
        self.in_act_fitness_sites = "Fitness_Sites.csv"
        self.in_act_cyclist_crashes = "Cyclist_Crashes.csv"
        self.in_tafe_campus_locations = "ACT_TAFE_Campus_Locations.csv"
        self.in_library_locations = "Library_Locations.csv"
        self.in_arts_facilities = "ACT_Arts_Facilities_List.csv"
        self.in_bbq = "Public_Barbeques_in_the_ACT.csv"
        self.in_public_furniture = "Public_Furniture_in_the_ACT.csv"
        self.in_playgrounds = "Town_And_District_Playgrounds.csv"
        self.in_dog_parks = "Fenced_Dog_Parks.csv"
        self.in_crime_stats = "ACT_CrimeStats_-_Jan2012_to_Mar2017"
        self.in_bus_data = "Bus_Stops_July_2017.csv"

        self.out_act_police_stations_locations = "safety_distance_to_police_stations.data"
        self.out_act_hospital_locations = "health_distance_to_hospitals.data"
        self.out_act_public_toilets = "safety_distance_to_public_toilets.data"
        self.out_act_fitness_sites = "health_distance_to_fitness_sites.data"
        self.out_act_cyclist_crashes = "transport_cyclist_crashes.data"
        self.out_tafe_campus_locations = "education_distance_to_tafe_campuses.data"
        self.out_library_locations = "education_distance_to_libraries.data"
        self.out_arts_facilities = "education_distance_to_art_facilities.data"
        self.out_bbq = "green_spaces_distance_to_bbqs.data"
        self.out_public_furniture = "green_spaces_distance_to_public_furniture.data"
        self.out_playgrounds = "green_spaces_distance_to_playgrounds.data"
        self.out_dog_parks = "green_spaces_distance_to_fenced_dog_parks.data"
        self.out_crime_stats = "safety_crime_stats_last_2.5_years.data"
        self.out_bus_data = "transport_bus_stops.data"

    def write_collection_of_points_to_file(self, points, file):
        with open(file, 'w+') as output_file:
            output_file.write('{"type": "FeatureCollection", "features": [')
            for index, point in enumerate(points):
                output_file.write(
                    '{"type": "Feature", "geometry": { "type": "Point", "coordinates": [' + str(point[0]) + ',' +
                    str(point[1]) + ']}, "properties": {"marker-size": "small"}}\n'
                )
                if len(points) != index+1:
                    output_file.write(',')
            output_file.write(']}')

    def get_distance(self, a, b):
        return great_circle(a, b).kilometers

    def print_distance_from_points_to_district_center(self, points, division_centers, path_to_file, invert=False):
        variable = (path_to_file[path_to_file.rfind('/')+1:len(path_to_file)-3])
        with open(path_to_file, 'w+') as file:
            points_to_write=[]
            for center in division_centers.keys():
                min_distance=sys.maxint
                dc = division_centers[center]
                for pd in points:
                    # print(dc, pd)
                    dist = self.get_distance(dc, pd)
                    if dist < min_distance:
                        min_distance=dist
                points_to_write.append([center, dc[0], dc[1], min_distance])

            np_points_to_write = np.array(points_to_write)
            min_dist = min(np_points_to_write[:,3])
            max_dist = max(np_points_to_write[:,3])

            # file.write("export const " + variable + " = [")
            for point in points_to_write:

                file.write("[{},{},{},{}]\n".format(
                    point[0],
                    point[1],
                    point[2],
                    self.normalize(float(min_dist), float(max_dist), float(point[3]), invert))
                )
            # file.write("]")

    def normalize(self, min, max, current, invert=False):
        ret_val = (float(current - min) / float(max - min)) * float(100.0)
        if invert:
            ret_val = 100.0 - ret_val
        return ret_val

    def process_act_division_boundaries(self):
        with open(self.raw_data_folder + "/" + self.in_act_division_boundaries) as input:
            ret_val = dict()
            lines = input.readlines()
            points = []
            for index, line in enumerate(lines):
                all_lat = 0.0
                all_lon = 0.0
                count = 0.0

                if index == 0:
                    continue

                sline = line.strip()
                division_name = sline[sline.find(')))",')+5:].split(",")[3]

                for coordinate in sline[sline.find("(((")+3: sline.find(")))")].split(","):
                    lat_lon = coordinate.strip().split(" ")
                    all_lon = all_lon + (float)(lat_lon[0])
                    all_lat = all_lat + (float)(lat_lon[1])

                    count = count + 1.0

                lon = all_lon / count
                lat = all_lat / count
                point = [lon, lat]
                ret_val[division_name] = point
                points.append(point)

        self.write_collection_of_points_to_file(
            points,
            self.output_folder + "/division_centers.json"
        )

        return ret_val

    def process_police_stations_locations(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_act_police_stations_locations, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                stripped_line = stripped_line[stripped_line.find('"'):]
                coordinates = stripped_line[stripped_line.find('(')+1:stripped_line.find(')')].strip()
                point = coordinates.split(', ')
                point = point[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_act_police_stations_locations,
            True
        )

    def process_hospital_locations(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_act_hospital_locations, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                stripped_line = stripped_line[stripped_line.find('"'):]
                coordinates = stripped_line[stripped_line.find('(')+1:stripped_line.find(')')].strip()
                point = coordinates.split(', ')
                point = point[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_act_hospital_locations,
            True
        )

    def process_public_toilets(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_act_public_toilets, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                points.append(stripped_line.split(',')[6:8][::-1])

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_act_public_toilets,
            False
        )

    def process_fitness_sites(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_act_fitness_sites, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                points.append(stripped_line.split(',')[6:8][::-1])

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_act_fitness_sites,
            True
        )

    def process_cyclist_crashes(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_act_cyclist_crashes, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                points.append(stripped_line.split(',')[8:10][::-1])

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_act_cyclist_crashes,
            False
        )

    def process_tafe_campus_locations(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_tafe_campus_locations, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind(',"(')+3:stripped_line.rfind(')"')].split(', ')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_tafe_campus_locations,
            True
        )

    def process_library_locations(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_library_locations, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind(',"(') + 3:stripped_line.rfind(')"')].split(', ')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_library_locations,
            True
        )

    def process_arts_facilities(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_arts_facilities, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind(',"(') + 3:stripped_line.rfind(')"')].split(', ')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_arts_facilities,
            True
        )

    def process_bbq(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_bbq, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind('",')+2:].split(',')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_bbq,
            True
        )

    def process_public_furniture(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_public_furniture, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind('",')+2:].split(',')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_public_furniture,
            True
        )

    def process_playgrounds(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_playgrounds, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind(',"(') + 3:stripped_line.rfind(')"')].split(', ')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_playgrounds,
            True
        )

    def process_fenced_dog_park(self, division_centers):
        with open(self.raw_data_folder + '/' + self.in_dog_parks, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                point = stripped_line[stripped_line.rfind(',"(') + 3:stripped_line.rfind(')"')].split(', ')[::-1]
                points.append(point)

        self.print_distance_from_points_to_district_center(
            points,
            division_centers,
            self.output_folder + '/' + self.out_dog_parks,
            True
        )

    def process_bus_data(self, division_centers):
        dp = DataPoints()
        dp.load_data()
        bus_stop_coordinates = []

        with open(self.raw_data_folder + '/' + self.in_bus_data, 'r') as input:
            points = []
            lines = input.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                stripped_line = line.strip()
                coordinates = stripped_line[stripped_line.find(",POINT (") + 8:stripped_line.find(")")]
                coordinatesar = coordinates.split(" ")
                # print(coordinatesar)
                bus_stop_coordinates.append(coordinatesar)

        dict_bus_stops_per_suburb = dp.get_number_of_bus_stops_per_suburb(bus_stop_coordinates)
        maxi = max(dict_bus_stops_per_suburb.values())
        mini = min(dict_bus_stops_per_suburb.values())

        with open(self.output_folder + '/' + self.out_bus_data, 'w') as output_file:
            for key in dict_bus_stops_per_suburb:
                cnt_bus_stops = (float(dict_bus_stops_per_suburb[key] - mini) / float(maxi - mini)) * float(100.0)
                if key.upper() in division_centers:
                    center = division_centers[key.upper()]
                    output_file.write('[{},{},{},{}]\n'.format(key.upper(), center[0], center[1], cnt_bus_stops))
                else:
                    print("Not there: " + key.uspper())
                    pass




        #         point = stripped_line[stripped_line.rfind(',"(') + 3:stripped_line.rfind(')"')].split(', ')[::-1]
        #         points.append(point)
        #
        # self.print_distance_from_points_to_district_center(
        #     points,
        #     division_centers,
        #     self.output_folder + '/' + self.out_bus_data,
        #     True
        # )

    def process_crime_stats(self, division_centers):
        print(division_centers)
        sum_of_all_crimes_2_5_years = dict()

        for year in ['2015', '2016', '2017']:
            file_name = self.raw_data_folder + '/' + self.in_crime_stats + "_" + year + ".csv"
            print(file_name)
            with open(file_name, 'r') as input:
                points = []
                lines = input.readlines()
                for index, line in enumerate(lines):
                    if index < 4:
                        continue

                    stripped_line = line.strip().split(",")
                    stripped_subset = [int(n) for n in line.strip().split(",")[2:] if n != '']

                    if stripped_line[1] != "":
                        suburb = stripped_line[1]
                        count_all_crimes = sum(stripped_subset)
                        # print(suburb, count_all_crimes, year)
                        if suburb in sum_of_all_crimes_2_5_years:
                            sum_of_all_crimes_2_5_years[suburb] = sum_of_all_crimes_2_5_years[suburb] + (count_all_crimes)
                        else:
                            sum_of_all_crimes_2_5_years[suburb] = count_all_crimes

        min_crime = min(sum_of_all_crimes_2_5_years.itervalues())
        max_crime = max(sum_of_all_crimes_2_5_years.itervalues())

        with open(self.output_folder + '/' + self.out_crime_stats, 'w') as output_file:
            for key in sum_of_all_crimes_2_5_years:
                crime = (float(sum_of_all_crimes_2_5_years[key] - min_crime) / float(max_crime - min_crime)) * float(100.0)
                crime = 100.0 - crime
                if key.upper() in division_centers:
                    center = division_centers[key.upper()]
                    output_file.write('[{},{},{},{}]\n'.format(key.upper(), center[0], center[1], crime))
                else:
                    # print("Not there: " + key.uspper())
                    pass

    def execute(self):
        division_centers = self.process_act_division_boundaries()
        # self.process_police_stations_locations(division_centers)
        # self.process_hospital_locations(division_centers)
        # self.process_fitness_sites(division_centers)
        # self.process_public_toilets(division_centers)
        # self.process_cyclist_crashes(division_centers)
        # self.process_tafe_campus_locations(division_centers)
        # self.process_library_locations(division_centers)
        # self.process_arts_facilities(division_centers)
        # self.process_bbq(division_centers)
        # self.process_public_furniture(division_centers)
        # self.process_playgrounds(division_centers)
        # self.process_fenced_dog_park(division_centers)
        # self.process_crime_stats(division_centers)
        self.process_bus_data(division_centers)

if __name__ == "__main__":
    preproc = DatasetPreprocessing()
    preproc.execute()