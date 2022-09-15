#!/usr/bin/env python3

def statcounter():
  stats = dict()

  def counter(n):
    if n not in stats:
      stats[n] = 0

    def fn(*args, **kwargs):
      stats[n] += 1
      return n(*args, **kwargs)
      
    return fn

  n = yield stats
  while True:
    n = yield counter(n)

# stat = statcounter()
# stats = next(stat)

# @stat.send
# def f1(a): return a+1

# @stat.send
# def f2(a, b): return f1(a)+f1(b)

# print(f1(f2(2,3)+f2(5,6)))
# print(*((f.__name__, c) for f, c in stats.items()))

# EOF