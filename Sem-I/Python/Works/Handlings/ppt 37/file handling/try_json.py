import json

data = {"name": "Alice", "age": 25}

#for writing json file

with open("data.json", "w") as f:

    json.dump(data, f)


#for reading json file

with open("data.json", "r") as f:
    content = json.load(f)
print(content)
print(content["name"])
