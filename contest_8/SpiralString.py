#!/usr/bin/env python3

# web crawling: http://uneex.org/LecturesCMC/PythonIntro2020/Homework_SpiralString/Review

from collections import Counter

class Spiral:

  def __init__(self, string = ""):
    self.cells = Counter(string)

  def __add__(self, other):
    return type(self)(self.cells + other.cells)

  def __sub__(self, other):
    return type(self)(self.cells - other.cells)

  def __mul__(self, num):
    return type(self)(list(self) * num)

  __rmul__ = __mul__

  def __len__(self):
    return sum(self.cells.values())

  def _square(self):

    # init arrays to calc direction
    dir_x, dir_y = (0, 1, 0, -1), (1, 0, -1, 0)

    dot = {}
    x = 0
    y = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0 

    turn_after = 0
    total_steps = 0
    direction = 0
    
    for i, c in enumerate(self):
      dot[x,y] = c
      min_x = min(min_x, x)
      min_y = min(min_y, y)
      max_x = max(max_x, x)
      max_y = max(max_y, y)
      if i >= turn_after:
        total_steps += 1
        turn_after += total_steps
        direction = (direction + 1) % 4

      x, y = x + dir_x[direction], y + dir_y[direction]
    return dot, (min_x, max_x), (min_y, max_y)

  def __iter__(self):
    return self.cells.elements()

  def __str__(self):
      dot, (min_x, max_x), (min_y, max_y) = self._square()
      return "\n".join("".join(dot.get((x,y), " ") for x in range(min_x, max_x+1)) for y in range(min_y, max_y+1))


# S = Spiral("abbcccddddeeeee")
# I = Spiral("abcdefghi")

# print(f"{S}\n")
# print(S+I, "\n")
# print(S-I, "\n")
# print(I*2, "\n")
# print(I*2-S, "\n")
# print(*list(S+I))

# EOF