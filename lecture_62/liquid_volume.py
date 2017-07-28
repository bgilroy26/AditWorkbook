import sys
import math


def liquid_volume(h):
    a = (4*math.pi*1000)/3 
    b = (math.pi *(h^2)*(30-h))/3
    return a - b

if __name__ == "__main__":
    print(str(liquid_volume(int(sys.argv[1]))))

