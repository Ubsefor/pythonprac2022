#!/usr/bin/env python3

dct = {}
res = []

while True:
  inpt = eval(input())

  if (inpt == (0, 0)):
    break

  if inpt[0] in dct:
    dct[inpt[0]].add(inpt[1])
  else:
    dct[inpt[0]] = {inpt[1]}

  #print(dct)
  if inpt[1] in dct:
    dct[inpt[1]].add(inpt[0])
  else:
    dct[inpt[1]] = {inpt[0]}

  #print(dct)


for i in dct:
  if (len(dct[i]) == (len(dct) - 1)):
    res.append(i)

res.sort()
print(*res)

# EOF