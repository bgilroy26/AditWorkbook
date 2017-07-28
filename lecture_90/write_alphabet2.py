import string

if __name__ == '__main__':
    f = open('alphabet2.txt', 'w')
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        f.write(letter1 + letter2 + '\n')

