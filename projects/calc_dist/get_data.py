import requests
import json


api_response = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
print(api_response.status_code)
api_data = api_response.json()
# print(api_response.status_code)

with open('meteor_data.json', 'w') as output_file:
    json.dump(api_data, output_file)
