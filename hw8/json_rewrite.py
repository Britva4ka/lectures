import json

with open('data.json') as f:
    data = json.load(f)
print(f"DATA {data}")
keys = []
values = []
for x in range(len(data['data'])): #Честно говоря я не до конца понял что от меня требовалось в этом задании.
    keys += data["data"][x].keys() #Как понял, так и сделал. Если что - поймите и простите.
    values += data["data"][x].values()
print(f'KEYS FROM DATA {keys}')
print(f"VALUES FROM DATA {values}")
split_format = {
    "columns": [
        keys[1],
        keys[2]
    ],
    keys[0]: [
        values[0],
        values[3]
    ],
    'data': [[
        values[1],
        values[2]
    ], [
        values[4],
        values[5]
    ]]
}

with open('split_format.json', 'w') as f:
    json.dump(split_format, f)
with open('split_format.json') as f:
    print(f.read())

index_format = {
    values[0]: {
    keys[1] : values[1],
    keys[2] : values[2]
    },
    values[3]: {
        keys[1] : values[-2],
        keys[2] : values[-1]
    }

}
with open('index_format.json', 'w') as f:
    json.dump(index_format, f)
with open('index_format.json') as f:
    print(f.read())
column_format = {
    keys[1]: {
        values[0] : values[1],
        values[3] : values[2]
    },
    keys[2]: {
        values[0] : values[-2],
        values[3] : values[-1]
    }
}
with open('column_format.json', 'w') as f:
    json.dump(column_format, f)
with open('column_format.json') as f:
    print(f.read())
