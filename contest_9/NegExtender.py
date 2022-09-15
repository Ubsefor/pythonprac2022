#!/usr/bin/env python3

class NegExt:
  def __neg__(self):
    wrapper = self.__class__

    try:
      return wrapper(super().__neg__())

    except Exception:
      try:
        end = -1
        beg = 1
        item = slice(beg, end)
        return wrapper(super().__getitem__(item))

      except Exception:
        return wrapper(self)

# class nstr(NegExt, str):
#     pass
# class nnum(NegExt, int):
#     pass
# class ndict(NegExt, dict):
#     pass
# print(-nstr("Python"), -nnum(123), -ndict({1: 2, 3: 4}), --nstr("NegExt"))

# EOF