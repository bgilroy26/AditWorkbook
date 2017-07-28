import sys

if __name__ == "__main__":
    count = 0
    f = open(sys.argv[1])
    for line in f:
        count = len(line.split())
    print(count)
