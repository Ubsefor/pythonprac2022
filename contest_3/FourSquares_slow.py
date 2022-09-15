import math


res = set()
n = int(input())
b = math.ceil(n ** 0.5)
for i in range(b + 1):
  i_2 = i ** 2
  for j in range(i, b + 1):
    j_2 = j ** 2
    for k in range(j, b + 1):
      k_2 = k ** 2
      s_2 = n - i_2 - j_2 - k_2
      if s_2 >= 0:
        s = s_2 ** 0.5
        if math.floor(s) ** 2 + i_2 + j_2 + k_2 == n:
          res.add(tuple(sorted([math.floor(s), i, j, k], reverse=True)))
        elif math.ceil(s) ** 2 + i_2 + j_2 + k_2 == n:
          pres.add(tuple(sorted([math.ceil(s), i, j, k], reverse=True)))
                    
for elem in sorted(res):
  print(' '.join(map(str, elem)))
