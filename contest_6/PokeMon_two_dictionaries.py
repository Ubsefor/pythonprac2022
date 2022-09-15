#!/usr/bin/env python3

D = dict()
D1 = dict()
D_res = dict()
res = []

while s:= input():

  s = s.split(" / ")

  if not s[0].isdigit():
    if s[0] in D:
      D[s[0]].append(s[1])
    else:
      D[s[0]] = [s[1]]

  else:
    if s[0] in D1:
      D1[s[0]].append(s[1])
    else:
      D1[s[0]] = []
      D1[s[0]].append(s[1])

for name, number in D.items():
  D_res[name] = len(set([i for j in number for i in D1[j]]))

D_res = {key: value for key, value in reversed(sorted(D_res.items(), key=lambda x: x[1]))}

for name, number in D_res.items():
  if number == max(D_res.values()):
    res.append(name)
  else:
    break

for item in sorted(res):
  print(item)

# EOF