#!/usr/bin/env python3

from decimal import *
import sys
# import math

getcontext().prec = 10000
sys.set_int_max_str_digits(100000)

def fact(n):
  sum = 1
  for i in range(2, n + 1):
    sum *= i
  return sum

def PiGen():
  k = 0
  sum = 0

  # chudn algo
  z = 426880 * Decimal("10005").sqrt()
  while True:
    nom = Decimal(str(fact(6 * k) * (13591409 + 545140134 * k)))
    denom = Decimal(str(fact(3 * k) * fact(k) ** 3 * (-262537412640768000) ** k))
    sum += nom / denom
    yield z / sum
    k += 1


# from time import time
# ctime = time()
# for p in PiGen():
#   if time()-ctime > 4:
#       break
# print(str(p)[5000:5070])

# EOF