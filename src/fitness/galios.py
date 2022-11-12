from fitness.base_ff_classes.base_ff import base_ff
import hashlib
import numpy as np
import math

class galios(base_ff):
    maximise = True  # True as it ever was.
    def __init__(self):
        self.testcase_list = []
        self.given_list = ["000", "001", "011", "101", "010", "110", "100", "111"]
        # self.num_obj = 2
        super().__init__()
                   
    def evaluate(self, ind, **kwargs):
        self.given_list = str(self.given_list)
        # self.testcase_list = ' '.join([str(elem) for elem in self.testcase_list])
        fitness = 0
        c = ind.phenotype
        print(c)
        temp = set(self.given_list)
        temp1 = set(self.testcase_list)
        a = temp.intersection(temp1)
        # hash1 = hashlib.sha256(c.encode())
        # print(hash1.hexdigest())
        # binary1 = bin(int(str(hash1.hexdigest()),16))
        
        # binary1= binary1[2:]
        # print(binary1)
        # fitness = self.calculate_entropy(str(binary1))+ 0.0298748   
        return int(len(c)) 
    
    
        
