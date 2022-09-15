#!/usr/bin/env python3

matrix = []
inpt = input().split()

matrix.append((min(int(inpt[0]), int(inpt[0]) + int(inpt[2])), 
              max(int(inpt[0]), int(inpt[0]) + int(inpt[2])), 
              min(int(inpt[1]), int(inpt[1]) + int(inpt[3])), 
              max(int(inpt[1]), int(inpt[1]) + int(inpt[3])),
              str(inpt[4]) 
            ))

x_min, x_max, y_min, y_max = matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]

while inpt := input().split():

  if int(inpt[2]) == 0 or int(inpt[3]) == 0:
    continue

  matrix.append((min(int(inpt[0]), int(inpt[0]) + int(inpt[2])), 
                max(int(inpt[0]), int(inpt[0]) + int(inpt[2])), 
                min(int(inpt[1]), int(inpt[1]) + int(inpt[3])), 
                max(int(inpt[1]), int(inpt[1]) + int(inpt[3])),
                str(inpt[4])
              ))

  if x_min > matrix[-1][0]:
    x_min = matrix[-1][0]

  if x_max < matrix[-1][1]:
    x_max = matrix[-1][1]

  if y_min > matrix[-1][2]:
    y_min = matrix[-1][2]

  if y_max < matrix[-1][3]:
    y_max = matrix[-1][3]


width  = abs(x_max - x_min)
height = abs(y_max - y_min)

image = [['.']*(width) for i in range(height)]

for rect in matrix:
  for i in range(rect[0], rect[1]):
    for j in range(rect[2], rect[3]):
      image[j - y_min][i - x_min] = rect[4]

for j in range(height):
  for i in range(width):
    print(image[j][i], end = '')
  print()

#EOF