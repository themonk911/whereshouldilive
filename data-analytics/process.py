#!/usr/bin/env python

import csv
import sys
from common_functions import ProcessSSCData

rent_csv="../datasets/2016Census_G36_ACT_SSC.csv"

# Read header
with open(rent_csv,'rb') as f:
    reader = csv.reader(f)
    header = next(reader)
    
i = 0
brackets = []
for col in header:
    prefix = col[:2]
    length = len(col)
    suffix = col[length-4:]
    if prefix == 'R_':
        if suffix == '_Tot':
            sections = col.split("_")
            lower = sections[1]
            upper = sections[2]
            col_idx = i
            if upper == "over":
                upper = int(lower)
            
            bracket = {
                "col_name" : col,
                "lower" : int(lower),
                "upper" : int(upper),
                "col_idx" : col_idx
            }
            brackets.append(bracket)
    i = i + 1

suburbs = []
ssc_obj = ProcessSSCData()
with open(rent_csv,'rb') as f:

    reader = csv.reader(f)
    for i,row in enumerate(reader):
        if (i == 0): continue
        ssc = row[0]

        suburb = {}
        code = int(ssc.replace("SSC", ""))
        name = ssc_obj.convert_ssc_to_suburb_name(code)
        if (name == False):
            continue

        suburb["ssc"] = code
        suburb["name"] = name
        
        suburb_sum = 0
        total_num_persons = 0
        for b in brackets:
            col_idx = b["col_idx"]
            num_person = int(row[col_idx])
            if num_person > 0:
                average_bracket = num_person*(b["upper"] + b["lower"]) / 2
                suburb_sum = suburb_sum + average_bracket
                total_num_persons += num_person
            else:
                average = 0

        if total_num_persons > 0:
            suburb_average = suburb_sum / total_num_persons
            suburb["average"] = suburb_average
        else:
            suburb["average"] = 0
        
        suburbs.append(suburb)

def write_suburbs_to_data (suburbs, outfile):    
    minn = 0
    maxx = 0
    for suburb in suburbs:
        num = suburb["average"]
        if (num <= minn):
            minn = num
        if (num >= maxx):
            maxx = num

    with open(outfile, "w") as f:
        for suburb in suburbs:
            normalised_average = 100.0 - (float(suburb["average"])-float(minn))/float(maxx - minn)*100
            #print ("[{}, 0, 0, {}]".format(suburb["name"], normalised_average))
            f.write("[{},0,0,{}]\n".format(suburb["name"], normalised_average))



write_suburbs_to_data(suburbs, sys.argv[1])