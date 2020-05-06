import json

with open('jawiki-country.json', 'r') as f:
    json_f = json.load(f)
    print(json_f)