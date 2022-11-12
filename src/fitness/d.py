import hashlib
import numpy as np
import math
import statistics
import pandas as pd
from decimal import Decimal
def estimated_autocorrelation(x):
        n = len(x)
        x = np.array(list(x))
        # x = pd.Series(x)
        print(x)
        result = np.correlate(x, x, mode='full')
    # return result[result.size/2:] 
        # x = Decimal(x.astype(np.int64))
        # # x = x.astype(int)
        # variance = np.var(x)
        # x = x-np.mean(x)
        # r = np.correlate(x, x, mode = 'full')[-n:]
        # assert np.allclose(r, np.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
        # result = r/(variance*(np.arange(n, 0, -1)))
        return result[result.size//2:]
                   
def evaluate(c1, **kwargs):
        fitness = 0
        # c1 = ind.phenotype
        hash1 = hashlib.sha512(c1.encode())
        # print(hash1.hexdigest())
        binary1 = bin(int(str(hash1.hexdigest()),16))
        
        binary1= binary1[2:]
        fitness = estimated_autocorrelation(binary1)
        print(fitness)
        return fitness
    
    
evaluate("x0M\(Qo@2Fp=0k3I*M5v0d\[I\[rW0N6h3t\]TI4j\]Hv&7O6r<Dj^3xB5:3l:DQ2f,>jN3H9n\\[kQ7m6B<i6V,=uP6t7U&Kq,6+K")