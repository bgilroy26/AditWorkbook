import json
import pprint

if __name__ == "__main__":
    with open("company1.json", "r") as file:
        d = json.load(file)
        pprint.PrettyPrinter(indent=4).pprint(d)

