inp = 0
pinp = float('-inf')
cnt = 0
pcnt = 0

while (True):
  inp = int(input())
  if (inp == 0):
    break
  if (inp >= pinp):
    cnt += 1
  else:
    if (cnt >= pcnt):
      pcnt = cnt
    cnt = 1
  pinp = inp
  
print (max(cnt, pcnt))