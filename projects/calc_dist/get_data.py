import requests
import json


meteor_response = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
meteor_data = meteor_response.json()
# print(meteor_response.status_code)

with open('meteor_data.json', 'w') as output_file:
    json.dump(meteor_data, output_file)
