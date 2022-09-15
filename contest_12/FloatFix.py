#!/usr/bin/env python3

import numbers
import types

class fixed(type):

  @classmethod
  def __prepare__(metacls, name, bases, **kwds):
    # print("prepare", name, bases, kwds)
    return super().__prepare__(name, bases, **kwds)
    

  @staticmethod
  def __new__(metacls, name, parents, ns, **kwds):
    # print("new", metacls, name, parents, ns, kwds)
    prec = kwds.get("ndigits", 3)

    def dec(fn):

      def fix(*args, **kargs):
        res = fn(*args, **kargs)
        if isinstance(res, numbers.Real):
          return round(res, prec)

        else:
          return res

      return fix

    for k in ns:
      if isinstance(ns[k], types.FunctionType):
        ns[k] = dec(ns[k])

    return super().__new__(metacls, name, parents, ns)


  def __init__(cls, name, parents, ns, **kwds):
    # print("init", cls, parents, ns, kwds)
    return super().__init__(name, parents, ns)


  def __call__(cls, *args, **kwargs):
    # print("call", cls, args, kwargs)
    return super().__call__(*args, **kwargs)


## TEST ##

# from fractions import Fraction
# from decimal import Decimal

# class C(metaclass=fixed, ndigits=4):
#     def div(self, a, b):
#         return a / b

# print(C().div(6, 7))
# print(C().div(Fraction(6), Fraction(7)))
# print(C().div(Decimal(6), Decimal(7)))

# EOF