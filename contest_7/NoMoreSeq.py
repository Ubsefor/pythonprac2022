#!/usr/bin/env python3

def nomore(sequence):
  for i in range(len(sequence)):
    for k in sequence:
      if k <= sequence[i]:
        yield k

# print(*nomore([n % 13 for n in range(5,23,3)]))

# EOF