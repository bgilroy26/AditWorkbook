import sys

def string_split(string):
    return len(string.split("_"))



if __name__ == "__main__":
    print(string_split(sys.argv[1]))
