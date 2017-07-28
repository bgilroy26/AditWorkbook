import string

if __name__ == '__main__':
    for letter in string.ascii_lowercase:
        filename = letter + '.txt'
        f = open(filename, 'w')
        f.write(letter + '\n')

