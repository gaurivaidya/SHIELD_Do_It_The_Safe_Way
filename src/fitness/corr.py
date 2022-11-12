from fitness.base_ff_classes.base_ff import base_ff
import hashlib
import numpy as np
import math
import matplotlib.pyplot as plt
class corr(base_ff):
    maximise = False  # True as it ever was.
    def __init__(self):
        super().__init__()
    
    def auto(self, binary1):
        len1 = len(str(binary1))
        arr = list(binary1)
        temp = list(binary1)
        N = 512
        v = 0
        for i in range(-511, 511):
            arr = np.roll(arr, i)
            A = N-np.sum(arr != temp )
            AC = abs(A-np.sum(arr != temp ))/N
            plt.plot(i, AC)
        
            v = v+AC
        # plt.show()
        return v/N
            # print(np.sum(arr != temp ))
            # f = open('a.txt','a')
            # f.write(str(i) +" " + str(AC) + '\n')
            # f.close()
                   
    def evaluate(self, ind, **kwargs):
        fitness = 0
        c1 = ind.phenotype
        hash1 = hashlib.sha3_512(c1.encode())
        # print(hash1.hexdigest())
        binary1 = bin(int(str(hash1.hexdigest()),16))
        fitness = self.auto(binary1)
        return fitness
    
    
        
