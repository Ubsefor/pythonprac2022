import math

res = []
n = int(input())
b_i = int(math.sqrt(n))
for i in range(b_i, -1, -1):
  b2_j = n-i**2
  b_j = int(math.sqrt(b2_j))
  for j in range(b_j, i-1, -1):
    b2_k = b2_j-j**2
    b_k = int(math.sqrt(b2_k))
    for k in range(b_k, j-1, -1):
      s2 = b2_k-k**2
      s = int(math.sqrt(s2))
      if s < k:
        continue
      if s**2 == s2:
        res.append([s,k,j,i])

for elem in sorted(res):
  print(' '.join(map(str, elem)))
