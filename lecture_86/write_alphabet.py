import string

if __name__ == '__main__':
    f = open('alphabet.txt', 'w')
    for letter in string.ascii_lowercase:
        f.write(letter + '\n')

