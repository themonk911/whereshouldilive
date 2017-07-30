#!/usr/bin/env python

import csv
import sys

sqlite_file = 'dbfile'

income_csv="2016Census_G36_ACT_SSC.csv"

# Read header
with open(income_csv,'rb') as f:
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
with open(income_csv,'rb') as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        if (i == 0): continue
        ssc = row[0]

        suburb = {}
        suburb["ssc"] = str(ssc.replace("SSC", ""))
        
        suburb_sum = 0
        suburb_brac_count = 0
        for b in brackets:
            col_idx = b["col_idx"]
            num_person = int(row[col_idx])
            if num_person > 0:
                average_bracket = (b["upper"] + b["lower"]) / num_person
                suburb_brac_count = suburb_brac_count + 1

                suburb_sum = suburb_sum + average_bracket
            else:
                average = 0

        if suburb_brac_count > 0:
            suburb_average = suburb_sum / suburb_brac_count
            suburb["average"] = suburb_average
        else:
            suburb["average"] = 0
       
        suburbs.append(suburb)

        



