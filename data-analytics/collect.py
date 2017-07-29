import os
import sys

class Collect:
    def __init__(self):
        self.folder = "/home/fpoppa/workspace/whereshouldilive/src/data"
        self.data = dict()
        self.header = []

    def execute(self):
        index = 0
        for file_name in sorted(os.listdir(self.folder)):
            with open(self.folder + '/' + file_name, 'r') as file:
                if file_name.endswith(".data"):
                    if index == 0:
                        self.header.append('district')
                        self.header.append('lon')
                        self.header.append('lat')
                        self.header.append(file_name[0:len(file_name)-3])
                    else:
                        self.header.append(file_name[0:len(file_name)-3])

                    for line in file.readlines():
                        sline = line.strip()
                        tmp1=sline.find('[')+1
                        tmp2=sline.find(']')
                        split_line = sline[tmp1:tmp2].split(',')
                        key = str(split_line[0])
                        if index == 0:
                            # print(str(split_line[0:2]))
                            self.data[key] = [
                                float(split_line[1]),
                                float(split_line[2]),
                                float(split_line[3])
                            ]

                            # sys.exit(1)
                            # print(self.data[key])
                        else:
                            if key in self.data:
                                value = self.data[key]
                                value2 = split_line[3]
                                # value3 = value.append(value2)
                                self.data[key].append(float(value2))

                            else:
                                print("Key not used yet: " + key)

                    index = index + 1

        with open("/home/fpoppa/workspace/whereshouldilive/src/data/summary_of_all_data.js", 'w') as result_file:
            sheader = str(self.header)
            result_file.write("//" + sheader[1:len(sheader)-1] + "\n")

            result_file.write("export const summary = [")
            for key in self.data:
                sdata = str(self.data[key])
                result_file.write('["' + str(key) + '", ' + sdata[1:len(sdata)-1] + "],\n")
            result_file.write("]")

if __name__ == "__main__":
    collector = Collect()
    collector.execute()