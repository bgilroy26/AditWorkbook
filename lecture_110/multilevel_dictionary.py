d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
    "owners":[{"firstName": "Jack", "lastName": "Petter"},
              {"firstName": "Jessy", "lastName": "Petter"}]}

if __name__ == "__main__":
    print(d["employees"][1]["lastName"])
    
