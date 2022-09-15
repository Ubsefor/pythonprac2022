s = input()
x_hi = y_hi = z_hi = float('-inf')
x_lo = y_lo = z_lo = float('inf')

while s != "":
  x, y, z = map(float, s.split(','))
  if (x > x_hi):
    x_hi = x
  if (x < x_lo):
    x_lo = x
  if (y > y_hi):
    y_hi = y
  if (y < y_lo):
    y_lo = y
  if (z > z_hi):
    z_hi = z
  if (z < z_lo):
    z_lo = z
  s = input()
  
print((x_hi - x_lo) * (y_hi - y_lo) * (z_hi - z_lo))
