def maxfun(s, *argv):

  sums = []
  for func in argv:
    current = 0

    for i in s:
      current += func(i)

    sums.append(current)

  max_s = sums[0]
  f = 0

  for i in range(0, argv.__len__()):
    if max_s < sums[i]:
      max_s = sums[i]
      f = i
    elif max_s == sums[i]:
      f = i

  return argv[f]

# from math import *
# print(maxfun(range(-2,10), sin, cos, exp)(1))