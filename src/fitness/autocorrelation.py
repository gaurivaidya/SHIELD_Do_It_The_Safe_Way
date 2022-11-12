from fitness.base_ff_classes.base_ff import base_ff
import hashlib
import numpy as np
import math
import statistics
import pandas as pd

class autocorrelation(base_ff):
    maximise = False  # True as it ever was.
    def __init__(self):
        self.ab = []
        super().__init__()
    
    def estimated_autocorrelation(self, x):
        n = len(x)
        x = pd.Series(x)
        x = x.astype(int)
        variance = x.var()
        x = x-x.mean()
        r = np.correlate(x, x, mode = 'full')[-n:]
        assert np.allclose(r, np.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
        result = r/(variance*(np.arange(n, 0, -1)))
        return result
                   
    def evaluate(self, ind, **kwargs):
        fitness = 0
        c1 = ind.phenotype
        hash1 = hashlib.sha3_512(c1.encode())
        # print(hash1.hexdigest())
        binary1 = bin(int(str(hash1.hexdigest()),16))
        
        binary1= binary1[2:]
        fitness = self.estimated_autocorrelation(binary1)
        return fitness
    
    
        
