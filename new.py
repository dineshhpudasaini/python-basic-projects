import json
with open(".json","r") as file:
    myjson = json.load(file)
    print(myjson)