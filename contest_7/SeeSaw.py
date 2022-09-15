#!/usr/bin/env python3

def seesaw(seq):

  from itertools import chain, tee, zip_longest # to fill missing with value

  t1, t2 = tee(seq, 2)

  odd_t1  = filter(lambda x: not x % 2, t1) 
  even_t2 = filter(lambda x: x % 2, t2)

  for i in zip_longest (odd_t1, even_t2):
    for elem in i:
      if (elem != None):
        yield elem

# print(*seesaw(i//3 for i in range (1, 27, 2)))

# EOF