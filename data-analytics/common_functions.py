#!/usr/bin/python
import sys

from preprocessing import DatasetPreprocessing


class ProcessSSCData:

	def __init__(self):
		ssc_src_file = "../datasets/SSC_2016_AUST_ACT.csv"
		self.dataobj = DatasetPreprocessing()
		self.division_centers = self.dataobj.process_act_division_boundaries()
		with open(ssc_src_file) as f:
			self.ssc_data = f.readlines()
		self.ssc_map = {}
		for line in self.ssc_data:
			split_array = line.split(",")
			code = int(split_array[1])
			suburb = split_array[2]
			if not suburb.find("ACT Remainder") or not suburb.find("Migratory") or not suburb.find("No usual"):
				continue
			suburb = suburb.replace(" (ACT)", "")
			suburb = suburb.upper()
			if (code not in self.ssc_map) and (suburb in self.division_centers):
				self.ssc_map[code] = suburb

		
	def convert_ssc_to_suburb_name(self, ssc):		
		if ssc in self.ssc_map:
			return self.ssc_map[ssc]
		else:
			return False

if __name__=="__main__":		
	ssc_obj = ProcessSSCData()
	print (ssc_obj.convert_ssc_to_suburb_name(80110))