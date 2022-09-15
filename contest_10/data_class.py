#!/usr/bin/env python3

def sloter(fields, default):
	class DataClass:
		__slots__ = fields

		def __init__(self):
			for item in DataClass.__slots__:
				self.__setattr__(item, default)

		def __iter__(self):
			res = list()
			for item in self.__slots__:
				res.append(getattr(self, item))
				
			return iter(res)

		def __delattr__(self, attrname):
			self.__setattr__(attrname, default)

	return DataClass


# s = sloter(("A", "b", "CC"), 100500)()
# print(*s)
# s.A, s.b, s.CC = 3, 2, 1
# del s.b
# print(*s)
# try:
#   s.E = 123
# except AttributeError:
#   print("No .E")

# EOF