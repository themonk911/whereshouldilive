#!/usr/bin/python
import sys
import ast

with open(sys.argv[1]) as f:
	grid_data = f.readlines()

with open(sys.argv[2]) as f:	
	summary_data = f.readlines()

# suburb points will be indexed by name
##	"points" : [()],
##	"heats": [],

def write_suburbs(suburbs, file_name, comment, variable):
	with open(file_name, "w") as f:
		f.write(comment + variable)
		for name in suburbs:
			suburb = suburbs[name]
			for point in suburb['points']:	
				string = '["{}",'.format(name)
				heat_str = ','.join([str(point[0])] + [str(point[1])] + [str(elt) for elt in suburb['heats']])
				f.write(string + heat_str + "],\n")
		f.write("]")

suburbs = {}

names = set()

for line in grid_data:	
	first_comma = line.find(",")
	name = line[:first_comma]
	array = line[first_comma + 1:].strip()
	array = ast.literal_eval(array)		
	suburbs[name] = {}
	suburbs[name]['points'] = array	
	names.add(name)



for line in summary_data[2:]:
	line = line.replace('[', '')
	line = line.replace(']', '')
	if (line.strip() != "\n"):		
		split_array = line.split(",")
		name = split_array[0][1:-1] # ignore ""
		heats = map(float, split_array[3:-1])
		if (name != ''):			
			if name not in names:
				print (name)
			suburbs[name]['heats'] = heats			

		
write_suburbs(suburbs, sys.argv[3], summary_data[0], summary_data[1])