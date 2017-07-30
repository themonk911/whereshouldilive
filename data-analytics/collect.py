import sys

class Collect:
    def __init__(self):
        self.headers = []

        self.input_folder = "../src/data"
        self.input_weighting = {
            'education': {
                 'education_distance_to_art_facilities.data': 0.1,
                 'education_distance_to_libraries.data': 0.2,
                 'education_distance_to_tafe_campuses.data': 0.7
            },
            'green_spaces': {
                'green_spaces_distance_to_bbqs.data': 0.3,
                'green_spaces_distance_to_fenced_dog_parks.data': 0.1,
                'green_spaces_distance_to_playgrounds.data': 0.3,
                'green_spaces_distance_to_public_furniture.data': 0.3
            },
            'safety': {
                'safety_distance_to_police_stations.data': 0.4,
                'safety_distance_to_public_toilets.data': 0.2,
                'safety_crime_stats_last_2.5_years.data': 0.4
            },
            'housing': {
                'weekly_rental_prices.data': 1.0
            },
            'transport': {
                'transport_cyclist_crashes.data': 0.2,
                'transport_bus_stops.data': 0.8
            },
            'health': {
                'health_distance_to_fitness_sites.data': 0.2,
                'health_distance_to_hospitals.data': 0.8
            }
        }

        self.output_summary_of_all_data = dict()

    def execute(self):
        first_time_header = True

        for category in sorted(self.input_weighting):
            print("category: " + category)
            overall_value_category = dict()
            number_of_values_in_category = 0

            if first_time_header:
                self.headers.append('district')
                self.headers.append('lon')
                self.headers.append('lat')
            self.headers.append(category)

            for file_name in self.input_weighting[category]:
                with open(self.input_folder + '/' + file_name, 'r') as file:
                    print("   Processing file " + file_name)
                    number_of_values_in_category += 1

                    for line in file.readlines():
                        stripped_line = line.strip()
                        split_line = stripped_line[stripped_line.find('[')+1:stripped_line.find(']')].split(',')
                        key = str(split_line[0])
                        print("      Key: " + key)

                        if first_time_header:
                            self.output_summary_of_all_data[key] = [
                                float(split_line[1]),
                                float(split_line[2])
                            ]

                        if key in overall_value_category:
                            overall_value_category[key].append(
                                self.input_weighting[category][file_name] * float(split_line[3])
                            )
                        else:
                            overall_value_category[key] = \
                                [self.input_weighting[category][file_name] * float(split_line[3])]

            first_time_header = False

            for key in overall_value_category:
                if key in self.output_summary_of_all_data:
                    self.output_summary_of_all_data[key].append(
                        sum(overall_value_category[key]) / number_of_values_in_category
                    )
                else:
                    self.output_summary_of_all_data[key] = [sum(overall_value_category[key]) / number_of_values_in_category]

        with open(self.input_folder + '/' + "summary_of_all_data.js", 'w') as result_file:
            sheader = str(self.headers)
            result_file.write("//" + sheader[1:len(sheader)-1] + "\n")

            result_file.write("export const summary = [\n")
            for key in self.output_summary_of_all_data:
                sdata = str(self.output_summary_of_all_data[key])
                result_file.write('["' + str(key) + '", ' + sdata[1:len(sdata)-1] + "],\n")
            result_file.write("]")

if __name__ == "__main__":
    collector = Collect()
    collector.execute()