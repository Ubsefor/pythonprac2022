from math import *
from sys import *

k = int(eval(input()))
 
if (k == 0 or k == 1):
  print(k)
  exit()

i = 1
while (True):
  i *= 10
  x = k * (i - k) // (10 * k - 1)
  
  if (x * 10 + k) * k == k * i + x:
    break

print(x * 10 + k)
