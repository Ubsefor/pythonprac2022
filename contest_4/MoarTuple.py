def moar(a, b, n):
  res_a = 0
  res_b = 0

  for i in a:
    res_a += (i % n) == 0

  for i in b:
    res_b += (i % n) == 0

  return res_a > res_b

#print(moar((25,0,-115,976,100500,7),(32,5,78,98,10,9,42),5))
