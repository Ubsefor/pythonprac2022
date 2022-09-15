#!/usr/bin/env python3 

import time

def sort_key(row):
  return [row[0], row[1][1], row[1][0], row[1][2]]


inpt = input().split()
lst = []
while inpt:
  lst.append([time.strptime(inpt[-1], "%H:%M:%S"), [inpt[0], inpt[1], ' '.join(inpt[2:len(inpt) - 1]), inpt[-1]]])
  inpt = input().split()

lst.sort(reverse=False, key=sort_key)

res = [lst[0][1]]
cnt = 0
idx = 0

while idx < (len(lst) - 1) and cnt < 3:
  idx += 1
  if lst[idx][0] != lst[idx - 1][0]:
    cnt += 1

  if cnt < 3:
    res.append(lst[idx][1])
        
lengths = [0] * len(res[0])
for row in res:
  for i in range(len(row)):
    if len(row[i]) > lengths[i]:
      lengths[i] = len(row[i])

for row in res:
  for i in range(len(row)):
    print('{:<{prec}}'.format(row[i], prec=lengths[i]), end=' ')
  print()

#EOF
