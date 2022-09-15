#!/usr/bin/env python3

s = input()
inpt = list()

classes = dict()

def delete_from_queue(del_cl, queue):
  for q in queue:
    if q and q[0] == del_cl:
      del q[0]
  return list(filter(len, queue))


def not_in_tail(elem, queue):
  return elem == queue[0] or elem not in queue


def merge(names):
  res = list()
  main_queue = list()
  for item in names:
    main_queue.append(classes[item].copy())

  while main_queue:
    for itm in main_queue:
      a = itm[0]
      if all(not_in_tail(a, elem) for elem in main_queue):
        res.append(a)
        main_queue = delete_from_queue(a, main_queue)
        break
      else:
        raise TypeError

  return res


try:
  while s != "":
    if s[0:5] == "class":
      s = s[6:]
      className = ""
      emptyClass = True
      l_brackets_idx = 0
      r_brackets_idx = 0

      if s.__contains__('('):
        l_brackets_idx = s.find('(')
        r_brackets_idx = s.find(')')
        className = s[:l_brackets_idx]
        emptyClass = False

      else:
        className = s[:s.find(':')]

      if className not in classes:
        names = list()

        if not emptyClass:
          names = s[l_brackets_idx+1:r_brackets_idx].split(',')
          names = [item.strip() for item in names]

        if len(names) == 0:
          classes[className] = [className]

        else:
          n_queue = list(className)

          if len(names) > 0:
            n_queue = [className, *merge(names)]

          classes[className] = n_queue

      else:
        raise TypeError

    else:
      s = input()
      continue

    s = input()

except TypeError:
  print('No')

else:
  print('Yes')

#EOF