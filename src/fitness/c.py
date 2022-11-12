import math
import hashlib

ab = []

class c():
    maximise = True  # True as it ever was.
    def __init__(self):
        self.m = []
        
   
    def genbin(self, n, bs=''):
        if len(bs) == n:
            ab.append(bs)
        else:
            self.genbin(n, bs + '0')
            self.genbin(n, bs + '1')
            return ab
    
    def CountOccurrences(self, string1, substring):
        count = 0
        start = 0
        while start < len(string1):
            pos = string1.find(substring, start)
            if pos != -1:
                start = pos + 1
                count += 1
            else:
                break
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
            print(en)
            en1 = en1 + (en/j)
            print(en1)
            cd.clear()
            freq.clear()
            # self.ab.clear()
        return en1 
    
    def ent(self, freq, sym):
        entropy = 0.0
        for i in range(0, sym):
            if freq[i] > 0.0:
                entropy += freq[i] * math.log(freq[i], 2)
        return -1 * entropy
                   
    def evaluate(self, ind, **kwargs):
        fitness = 0
        c = ind
        # print(c)
        hash1 = hashlib.sha512(c.encode())
        # print(hash1.hexdigest())
        binary1 = bin(int(str(hash1.hexdigest()),16))
        
        binary1= binary1[2:]
        # print(binary1)
        fitness = self.calculate_entropy(str(binary1))
        print(fitness)
        return fitness

v = c()
b = v.calculate_entropy("10100101010101011101101100110110000101011110010100110001110101001100101101011101011111001101111100001010001011100000011010111111001111110001001111001110000010101101110111011101110011101110101000011001110001110001111001111011111111010111111011101000001001001101000011100110000101111000110100011010111100101000011011011001011110101000110110100100001101101011111110111111111110011001000011111000111101011000101101111011000000011100001011011000110111011001101111111110101111100011010100110010110100110011001111011")

    
        
