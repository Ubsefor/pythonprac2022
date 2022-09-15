string = eval(input())
numbers = []

for i in string:
  if type(i) == tuple:
    for j in i:
      numbers.append(j)
  else:
    if i > numbers.__len__():
      exit(0)
    print(tuple(numbers[:i]))
    numbers = numbers[slice(i, numbers.__len__())]
