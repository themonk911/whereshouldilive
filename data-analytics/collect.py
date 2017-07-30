import sys

class Collect:
    def __init__(self):
        self.headers = []

        self.input_folder = "../src/data"
        self.input_weighting = {
            'education': {
                 'education_distance_to_art_facilities.data': 1.0,
                 'education_distance_to_libraries.data': 1.0,
                 'education_distance_to_tafe_campuses.data': 1.0
            },
            'green_spaces': {
                'green_spaces_distance_to_bbqs.data': 1.0,
                'green_spaces_distance_to_fenced_dog_parks.data': 1.0,
                'green_spaces_distance_to_playgrounds.data': 1.0,
                'green_spaces_distance_to_public_furniture.data': 1.0
            },
            'safety': {
                'safety_distance_to_police_stations.data': 1.0,
                'safety_distance_to_public_toilets.data': 1.0
            },
            # 'housing': {
            #
            # },
            'transport': {
                'transport_cyclist_crashes.data': 1.0
            },
            'health': {
                'health_distance_to_fitness_sites.data': 1.0,
                'health_distance_to_hospitals.data': 1.0
            }
        }

        self.output_summary_of_all_data = dict()

    def execute(self):
        first_time_header = True

        for category in self.input_weighting:
            print("category: " + category)
            overall_value_category = dict()
            number_of_values_in_category = 0
            # index = 0

            if first_time_header:
                self.headers.append('district')
                self.headers.append('lon')
                self.headers.append('lat')
                print("Header: district, lat, lon")
            self.headers.append(category)
            print("Header: " + category)

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
                            first_time_header = False

                        if key in overall_value_category:
                            overall_value_category[key].append(
                                self.input_weighting[category][file_name] * float(split_line[3])
                            )
                            # print('2')
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

            result_file.write("export const summary = [")
            for key in self.output_summary_of_all_data:
                sdata = str(self.output_summary_of_all_data[key])
                result_file.write('["' + str(key) + '", ' + sdata[1:len(sdata)-1] + "],\n")
            result_file.write("]")

if __name__ == "__main__":
    collector = Collect()
    collector.execute()