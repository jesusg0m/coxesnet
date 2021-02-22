import scrapy
import json

def write_json(data, filename='mercedes.json'):
    with open (filename, 'w') as f:
        json.dump(data, f, indent=4)

with open ('mercedes.json') as json_file:
    data = json.load(json_file)
    temp = data['modelo']
    y = {'firstname': 'joe', 'age': 40}
    temp.append(y)

write_json(data)