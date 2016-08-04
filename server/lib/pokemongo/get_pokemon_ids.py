import requests
import json

json_data = None

with open("D:\\pokemon.json") as json_file:
    json_data = json.load(json_file)
    
for row in json_data:
    print '{0};{1}'.format(row['id'], row['name'])
