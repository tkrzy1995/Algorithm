#
# 
# sigmoid function v1
#
# author : tkrzy1995
#
#

import math

def sigmoid(x):
    
    return 1 / (1 + math.exp(-x)) 

x = float(input())
print(sigmoid(x))
