src = input()
substr = input()
 
if (substr == ""):
  print("YES")
  exit(0)
if len(src) == 1 or len(substr) == 1:
  if (substr in src):
    print("YES")
  else:
    print("NO")
  exit(0)

for i in range(1, len(src) // (len(substr) - 1) + 1):
  for j in range(i):
    if substr in src[j::i]:
      print("YES")
      exit(0)

print("NO")
exit(0)