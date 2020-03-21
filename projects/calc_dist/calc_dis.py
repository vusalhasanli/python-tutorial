import os
import json
import math
from haversine import calc_dist

with open('meteor_data.json', 'r') as input_file:
    meteor_data = json.load(input_file)
print(meteor_data[0]['reclat'])

# for meteor in meteor_data:
    # print(meteor)



my_location = ('37.499376', '-122.252775')



# calc_dist()