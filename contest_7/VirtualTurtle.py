#!/usr/bin/env python3

def turtle(coord, direction):
  pos = list(coord)
  # map coords for directions
  ways = {0: [1,0], 1: [0,1], 2: [-1,0], 3: [0,-1]}
  step = yield tuple(pos)
  
  while step:
    direct = ways[direction]
    if step == 'f':
      pos[0] += direct[0]
      pos[1] += direct[1]

    if step == 'l':
      direction = (direction + 1) % 4

    if step == 'r':
      direction = (direction - 1) % 4

    step = yield tuple(pos)

# robo = turtle((5,6),1)
# start = next(robo)
# for c in "flfrffrffr":
#     print(*robo.send(c))

# x, a, c, m = 3, 1366, 1283, 6075 
# robo = turtle((0, 0), 0)
# next(robo)
# for cmd in ("ffflr"[(x:=(a*x+c)%m)//2%5] for i in range(200)):
#     res = robo.send(cmd)
# print(res)

# EOF