import os
import json
import math
from haversine import calc_dist

with open('./projects/calc_dist/meteor_data.json', 'r') as input_file:
    meteor_data = json.load(input_file)

city_name = 'Tomakovka' # ------>> input() for future

for cities in meteor_data:
    if cities['name'] == city_name:
        lat1 = float(cities['reclat'])
        lon1 = float(cities['reclong'])

my_location = { "lat": 37.499376, "lon": -122.252775 }
distance = calc_dist(lat1, lon1, my_location['lat'], my_location['lon'])
print("Distance to the given location is: {}km".format(distance))

