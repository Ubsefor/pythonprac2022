#!/usr/bin/env python3

import types
import inspect

class init(type):

  @classmethod
  def __prepare__(metacls, name, bases, **kwds):
    # print("prepare", name, bases, kwds)
    return super().__prepare__(name, bases, **kwds)

  @staticmethod
  def __new__(metacls, name, parents, ns, **kwds):
    for i in ns:

      if isinstance(ns[i], types.FunctionType):
        fn = ns[i]

        def try_call(f):
          try:
            return f()

          except:
            return None

        anns = inspect.get_annotations(fn)
        arg_specs = inspect.getfullargspec(fn)

        defs = arg_specs[3]

        if defs:
          args = arg_specs[0][1:-len(defs)]
          defs = tuple([try_call(anns[name]) for name in args]) + defs
        else:
          args = arg_specs[0][1:]
          defs = tuple([try_call(anns[name]) for name in args])

        fn.__defaults__ = defs

    return super().__new__(metacls, name, parents, ns)

  def __init__(cls, name, parents, ns, **kwds):
    # print("init", cls, parents, ns, kwds)
    return super().__init__(name, parents, ns)


  def __call__(cls, *args, **kwargs):
    # print("call", cls, args, kwargs)
    return super().__call__(*args, **kwargs)

## TEST

# class C(metaclass=init):
#     def __init__(self, var: int, rng: range, lst: list[int], defined: str = "defined"):
#         self.data = f"{var}/{rng}/{lst}/{defined}"

# for c in (C(), C(1, range(3)), C(rng=range(4, 7)), C(lst=[1, 2, 3], defined=3)):
#     print(c.data)


# EOF