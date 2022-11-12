from fitness.base_ff_classes.base_ff import base_ff
import hashlib
import numpy as np
import math

class entropy(base_ff):
    maximise = True  # True as it ever was.
    def __init__(self):
        self.ab = []
        # self.num_obj = 3
        super().__init__()
        
   
    def genbin(self, n, bs=''):
        if len(bs) == n:
            self.ab.append(bs)
        else:
            self.genbin(n, bs + '0')
            self.genbin(n, bs + '1')
            return self.ab
    
    def CountOccurrences(self, string1, substring):
        count = 0
        start = 0
        while True:
            start = string1.find(substring, start) + 1
            if start > 0:
                count = count+1
            else:
                return count
        
    def calculate_entropy(self, binary1):
        en1 = 0.0
        en = 0.0
        y = len(binary1)
        for j in range(1,9):
            cd = []
            freq = []
            cd = self.genbin(j)
            # print(cd)
            for i in range(0, len(cd)):
                  m = self.CountOccurrences(binary1, cd[i])
                  freq.append(m)
            r=y-j+1
            for k in range(0, int(math.pow(2, j))):
                  freq[k]= freq[k]/r
            en = self.ent(freq, int(math.pow(2,j)))
            # print(en)
            en1 = en1 + (en/j)
            # print(en1)
            cd.clear()
            freq.clear()
            self.ab.clear()
        return en1 
    
    def ent(self, freq, sym):
        entropy = 0.0
        for i in range(0, sym):
            if freq[i] > 0.0:
                entropy += freq[i] * math.log(freq[i], 2)
        return -1 * entropy
                   
    def evaluate(self, ind, **kwargs):
        fitness = 0
        c = ind.phenotype
        # print(c)
        # hash1 = hashlib.sha3_512(c.encode())
        # print(hash1.hexdigest())
        import binascii
        binary1 = ''.join(format(ord(x), '08b') for x in str(c)) 
        # binary1 = bin(int(str(c)))
        
        binary1= binary1[2:]
        # print(binary1)
        fitness = self.calculate_entropy(str(binary1))+ 0.0298748  
        # if fitness>=7.9:
        #     f = open("unique_individuals.txt",'a')
        #     f.writelines(str(ind.phenotype)+'\t')
        #     f.writelines(str(fitness) + '\n')
        #     f.close() 
        return fitness 
    
    
        
