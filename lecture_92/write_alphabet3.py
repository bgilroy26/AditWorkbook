import string

if __name__ == '__main__':
    f = open('alphabet3.txt', 'w')
    for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
        f.write(letter1 + letter2 + letter3 + '\n')
    f.write("yz/n")

