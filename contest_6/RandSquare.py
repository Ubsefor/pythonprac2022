#!/usr/bin/env python3

def randsquare(A, B):
  import random
  
  diag_len = ((abs(A[0] - B[0]) ** 2 + abs(A[1] - B[1]) ** 2) ** (1 / 2))

  side = (diag_len ** 2 / 2) ** (1 / 2)

  cos_a = abs(A[0] - B[0]) / diag_len
  sin_a = abs(A[1] - B[1]) / diag_len
  # tg 45, as a coef
  q = 1 / (2 ** (1/2))

  # correct sign for sin and cos
  if B[0] < A[0]:
    cos_a = -cos_a

  if B[1] < A[1]:
    sin_a = -sin_a

  # random dot using length of square side
  x = random.uniform(0, side)
  y = random.uniform(0, side)

  # multiply by coeff to make sure not to step out
  x1 =   x * q + y * q
  y1 = - x * q + y * q

  # getting a dot into the square
  x_res =   x1 * cos_a - y1 * sin_a + A[0]
  y_res = + x1 * sin_a + y1 * cos_a + A[1]

  return (x_res, y_res)


# def showgr(Dots, Corners, Name="Dots"):
#   import numpy as np
#   import matplotlib.pyplot as plt

#   X, Y = zip(*Dots)
#   fig, ax = plt.subplots(num=Name)
#   ax.set_aspect(1)
#   ax.scatter(X, Y)
#   ax.fill(*Corners, fill=False)
#   plt.show()

# def show(A, B, num=1000):
#   dots = [randsquare(A, B) for i in range(num)]
#   R = [ (A[0], (B[0]+A[0])/2-(B[1]-A[1])/2, B[0], (B[0]+A[0])/2+(B[1]-A[1])/2),
#     (A[1], (B[1]+A[1])/2+(B[0]-A[0])/2, B[1], (B[1]+A[1])/2-(B[0]-A[0])/2)]
#   showgr(dots, R)

# show((6,7), (2,12), 5000)

# EOF