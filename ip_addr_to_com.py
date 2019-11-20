from bcc import BPF
import pyroute2
import time
import sys
from ctypes import *

primal = '192.168.1.2'

marker = primal.find('.')
one = int(primal[0:primal.find('.')])
primal = primal[marker+1:]
marker = primal.find('.')
two = int(primal[0:marker])
primal = primal[marker+1:]
marker = primal.find('.')
three = int(primal[0:marker])
primal = primal[marker+1:]
four = int(primal[0:])
primal = primal[marker+1:]
one = "{0:b}".format(one).zfill(8)
two = "{0:b}".format(two).zfill(8)
three = "{0:b}".format(three).zfill(8)
four = "{0:b}".format(four).zfill(4)
seq = (four, three, two, one)
result = ''.join(seq)
print("\n")
#result = ''.join(one)
print(result)


