import os
import json
import math
from haversine import calc_dist

my_location = { "lat": 37.499376, "lon": -122.252775 }


# 1. -------- >>
# with open('./projects/calc_dist/meteor_data.json', 'r') as input_file:
#     meteor_data = json.load(input_file)

# city_name = 'Tomakovka' # ------>> input() for future

# for cities in meteor_data:
#     if cities['name'] == city_name:
#         lat1 = float(cities['reclat'])
#         lon1 = float(cities['reclong'])

# my_location = { "lat": 37.499376, "lon": -122.252775 }
# distance = calc_dist(lat1, lon1, my_location['lat'], my_location['lon'])
# print("Distance to the given location is: {}km".format(distance))
# ------------------------- >>


# 2. ------------- >>

with open('./projects/calc_dist/meteor_data.json', 'r') as input_file:
    meteor_data = json.load(input_file)

    for meteor in meteor_data:
        if not ('reclat' in meteor and 'reclong' in meteor): continue
        meteor['distance'] = calc_dist(float(meteor['reclat']),
        float(meteor['reclong']), my_location['lat'], my_location['lon'])
# print(meteor_data)


with open('./projects/calc_dist/meteor_data1.json', 'w') as output_file:
    json.dump(meteor_data, output_file)


