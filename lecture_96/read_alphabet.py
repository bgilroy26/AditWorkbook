import string

def read_alphabet():


    alphabet = []

    for letter in string.ascii_lowercase:
        f = open(letter + '.txt', 'r')

        alphabet.append(f.read().rstrip())

    return alphabet



if __name__ == '__main__':
    print(read_alphabet())
