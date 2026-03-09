import json
data = "hello world once again"
with open("sample.txt","w") as f:
     json.dump(data, f)
with open("sample.txt","r") as f:
        content = json.load(f)
print(content)
print(type(content))
