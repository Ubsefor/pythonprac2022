#!/usr/bin/env python3

class Nuts:

  def __init__(self, *args):
    pass
  
  def __getitem__(self, idx):
    return idx

  def __getattribute__(self, attr):
    return attr
  
  def __setitem__(self, idx, val):
    pass

  def __setattr__(self, attr, val):
    pass
  
  def __delitem__(self, idx):
    pass
  
  def __delattr__(self, attr):
    pass
  
  def __str__(self):
    return "Nuts"
  
  def __iter__(self):
    for i in 'Nuts':
    	yield i
  
  def __next__(self):
    raise StopIteration
    
    
# M, N = Nuts(), Nuts(1,2,3,4)
# print(M, N)
# M[100] = N.qwerty = 42
# print(M[100], N.qwerty)
# print(*list(Nuts("QWERQWERQWER")))
# del M["QQ"], N[6:10], M[...], N._, N.qwerty
# print(M.asdfg, N[-2])

# EOF