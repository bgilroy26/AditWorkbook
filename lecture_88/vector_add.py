import itertools
import pprint
import sys

def vector_add(*vectors):
    #throw error if vector length mismatch
    if len(set(map(len, vectors))) != 1:
        raise ValueError('vectors are not of equal length')
    
    resultant_vector = map(sum, [(vectors[0][0], vectors[1][0]), (vectors[0][1], vectors[1][1]), (vectors[0][2], vectors[1][2])])
    for component in list(resultant_vector):
        print(component)
    
    
    

if __name__ == '__main__':
    # data
    a = [1, 2, 3]
    b = (4, 5, 6)
    x = [a, b]

    vector_add(*x)
