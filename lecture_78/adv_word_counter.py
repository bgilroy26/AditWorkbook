import sys


if __name__ == "__main__":
    f = open(sys.argv[1])
    
    line = f.readline()

    line2 = line.split(",")

    line3 = " ".join(line2)

    print(len(line3.split()))
