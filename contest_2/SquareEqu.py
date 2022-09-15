a, b, c = map(int, input().split(','))

if (a == 0):
  if (b != 0):
    print(-c / b)
  else:
    if (c == 0):
      print(-1)
    else:
      print(0)
else:
  d = b ** 2 - 4 * a * c
  if (d == 0):
    print(-b / (2 * a))
  elif (d > 0):
    res = sorted(
      ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))
    )
    print(res[0], res[1])
  else:
    print(0)
