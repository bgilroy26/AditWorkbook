import json

if __name__ == "__main__":
    with open("company1.json", "r") as file:
        d = json.load(file)

    d["employees"].append({"firstName":"Albert", "lastName":"Bert"})

    with open("company1.json", "w") as file:
        json.dump(d, file, indent=4, sort_keys=True)

