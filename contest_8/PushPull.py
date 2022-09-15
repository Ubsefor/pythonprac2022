#!/usr/bin/env python3

class Pushpull:

  step = [0] 

  def __init__(self, s = 0):
    self.step[0] = s

    
  def __iter__(self):
    sign = 1
    if self.step[0] < 0:
      sign = -1
      
    for i in range(0, self.step[0], sign):
      yield i

    pass

  
  def __str__(self):
    if self.step[0] < 0:
      return '<' + str(abs(self.step[0])) + '<'

    elif self.step[0] == 0:
      return '<' + str(self.step[0]) + '>'

    elif self.step[0] > 0:
      return '>' + str(self.step[0]) + '>'

  def push(self, r = 1):
    self.step[0] = self.step[0] + r
    
  
  def pull(self, l = 1):
    self.step[0] = self.step[0] - l


# a = Pushpull(-10)
# print(a)
# b, c = Pushpull(7), Pushpull(5)
# print(b)
# for i in b:
#     c.pull()
# print(a)
# b.push(3)
# t = tuple(c)
# a.pull(7)
# t += tuple(b)
# print(*t)

# EOF