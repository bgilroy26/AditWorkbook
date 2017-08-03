import string
import sys

def validate_has_number(user_password):
    if any(i.isdigit() for i in user_password): 
        return True
    return False

def validate_has_upper(user_password):
    if any(i.isupper() for i in user_password):
        return True
    return False
    
def validate_length(user_password):
    if len(user_password) > 5:
        return True
    return False

usernames = ['Mercury','Venus','Earth', 'Mars','Jupiter','Saturn', 'Uranus','Neptune']

while True:
    uname = input("Enter username: ")
    if uname not in usernames:
        break
    print("Username is taken")

while True:
    notes = []
    pword = input("Enter new password: ")


    if not validate_has_number(pword):
        notes.append("Password must have at least 1 number")

    if not validate_has_upper(pword):
        notes.append("Password must have at least 1 uppercase letter")

    if not validate_length(pword):
        notes.append("Password must be at least 6 characters long")
                
    if len(notes) > 0:
        print("Password is not fine")

        for advisory in notes:
            print(advisory)
    else:
        print("Password is fine")
        break


