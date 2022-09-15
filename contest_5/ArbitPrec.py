#!/usr/bin/env python3

from decimal import Decimal, getcontext

def _eval(func, x):
  res = eval(func)
  return res


func = input()
d_input = int(input())
getcontext().prec = d_input + 2


# Approximation
left = Decimal('-1.5')
left_val = _eval(func, left)

right = Decimal('1.5')
right_val = _eval(func, left)

zero = Decimal('0')

while right_val != zero and (right-left) > 10 ** (-d_input):
  avg = (right + left) / 2
  avg_val = _eval(func, avg)

  if avg_val > 0 and left_val > 0 or avg_val < 0 and left_val < 0:
    left = avg
    left_val = avg_val

  else:
    right = avg
    right_val = avg_val

print('{:.{prec}f}'.format(right, prec=d_input))

#EOF