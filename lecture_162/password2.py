import string

def validate(user_password):
    if any(i.isdigit() for i in user_password) and any(i.isupper() for i in user_password) and len(user_password) > 5:
        return True
    return False

pword = input("Enter new password: ")

if validate(pword):
    print("Password is fine")
else:
    print("Password is not fine")


