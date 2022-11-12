import subprocess
import math
import time
import hashlib
import string
from random import random
import binascii
import os
import random

# for uniform number
def uniformrand():
	random.seed(9895);
	print("The 5 random number generated between 100 and 200 are : ");
	for i in range(1,10):
		print(round(random.uniform(100, 200)));
	print(); 

# taking seed from GE
def initial_seed(): # required to initiate prng
	os.system("python ponyge.py --parameters entropy_many.txt")
	
# keys with size 512
def key512(option, a):
	initial_seed()
	start=time.time()
	f = open("indi1.txt", "r")
	read_lines=f.readlines()
	lines=read_lines[-1]
	f.close();		
	v=0
	for i in range(1,a):
		a= str(i)+lines
		result = hashlib.sha512(a.encode())
		if option is not None:
			if option == 'prime':
				s=int(str(result.hexdigest()),16)
				b=miller_rabin.miller_rabin(s)
				if(b==1):
					v=v+1
					print(s)
			if option == 'digit':
				s=int(str(result.hexdigest()),16)
				print(s)
			if option == 'binary':
				print(bin(int(str(result.hexdigest()),16))) 
		else:
			print(result.hexdigest())

