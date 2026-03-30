import json

data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "creedits": 4}
    ]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("data.json has been created.")
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(f"Name: {loaded_data['name']}") 