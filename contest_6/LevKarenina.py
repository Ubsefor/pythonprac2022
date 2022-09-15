#!/usr/bin/env python3

# В первой строке ввода находится четыре символа: 

# знак препинания в конце предыдущего предложения p, 
# первая буква слова в начале предложения b, 
# первая буква последнего слова в предложении g,
# знак препинания в конце предложения e. 

# Все остальные строки, кроме последней, непустые, и содержат строки некоторого текста. 
# Текст состоит из слов (последовательностей любых непробельных символов) и пробелов. 
# Считается, что «предложение» — это то, что заканчивается на p или e. Вывести в предлагаемой форме

# - самое популярное слово,
  # & начинающееся на b,
  # & в начале предложений,
  # & перед которыми стояло p

# - самое популярное слово
  # & начинающееся на g,
  # & в конце предложений,
  # & заканчивающихся на e

# а также количество вхождений таких критериев.
# .Sf!
# <text>

from collections import Counter

# get first letters
p, b, g, e = input()

d1 = Counter()
d2 = Counter()
count_1 = '' 
count_2 = ''
flag = False

while (inpt:= input()):
  text = inpt.split()

  for word in text:
    # & начинающееся на g,
    # & в конце предложений,
    # & заканчивающихся на e
    if word[0] == g and word[-1] == e:
      d2.update([word])

    # & начинающееся на b,
    # & в начале предложений,
    # & перед которыми стояло p
    if word[0] == b and flag:
      d1.update([word])

    # set or unset flag for sentence, ending in p
    if word[-1] == p:
      flag = True
    else:
      flag = False

# print(d1)
# print(d2)

# most_common([n])
# Return a list of the n most common elements and their counts from the most common to the least. 
# If n is omitted or None, most_common() returns all elements in the counter. 
if d1:
  # d1.most_common(1)[0] -> ('Salves', 2)
  count_1 = (d1.most_common(1)[0])[0]

if d2:
  count_2 = (d2.most_common(1)[0])[0]

# print(d1[count_1])
# print(d2[count_2])

if count_1 != '':
  print(f"{count_1} {d1[count_1]} - ", end = '')
else:
  print(f"... 0 - ", end = '')

if count_2 != '':
  print(f"{count_2} {d2[count_2]}")
else:
  print(f"... 0")

# EOF