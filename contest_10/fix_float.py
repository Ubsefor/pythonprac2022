#!/usr/bin/env python3

def fix(n):
  def decorator(fn):
    def wrapper(*args, **kwargs):
      n_arg = []
      for i in args:
        if isinstance(i, float):
          n_arg.append(round(i, n))
        else:
        	n_arg.append(i)

      for j, k in kwargs.items():
        if isinstance(k, float):
          kwargs[j] = round(k, n)

      res = fn(*n_arg, **kwargs)
      if isinstance(res, float):
      	return round(res, n)
      else:
      	return res
    return wrapper
  return decorator

# @fix(4)
# def aver(*args, sign=1):
#     return sum(args)*sign

# print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))

# assert("-13.1916" == str(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1)))

# @fix(2)
# def to_string(value):
#     return str(value)
# print(to_string(0.1234)) # 0.12

# EOF