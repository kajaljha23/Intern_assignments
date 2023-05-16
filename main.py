import json

f = open('sample_data.json')
data = json.load(f)

result = []
for item in data['parametersList']:
    parameters = {
        "parameterName": item['parameterName'],
        "max": item['max'],
        "min": item['min'],
        "avg": item['avg']
    }
    result.append(parameters)
    print(result)
with open('new_sample_data.json', 'w') as f:
    json.dump(result, f, indent=2, sort_keys=True)
