from fitness.base_ff_classes.base_ff import base_ff
import hashlib
import numpy as np
import math
import random
from scipy.spatial.distance import hamming 


class hamming_distance(base_ff):
    maximise = True  # True as it ever was.
    def __init__(self):
        self.ab = []
        self.f = open("prng/indi.txt", "r")
        self.read_lines=self.f.readlines()
        self.c2 = self.read_lines[-1]
        self.f.close()
        super().__init__()
    
    def hammingDist(self, str1, str2):
        return sum(a1 != a2 for a1, a2 in zip(str1, str2))
                   
    def evaluate(self, ind, **kwargs):
        c1 = ind.phenotype
        v1 = random.randint(1, 10000)
        hash1 = hashlib.sha3_512(c1.encode())
        # print(hash1.hexdigest())
        binary1 = bin(int(str(hash1.hexdigest()),16))
        
        binary1= binary1[2:]
        # print(len(binary1))
        arr1 = list(binary1)
        # print(binary1)
        hash2 = hashlib.sha3_512(self.c2.encode())
        # print(hash1.hexdigest())
        binary2 = bin(int(str(hash2.hexdigest()),16))
        # print("\n\n\n\n")
        binary2= binary2[2:]
        # print(len(binary2))
        arr2 = list(binary2[ 0 : len(binary1) ])

        # print(binary2)
        
        f = open("prng/indi.txt", "a")
        f.write(c1+"\n")
        f.close()
        # print(c1)
        # print(self.c2)
        fitness = self.hammingDist(binary1, binary2)
        return (fitness)

    
    
        
