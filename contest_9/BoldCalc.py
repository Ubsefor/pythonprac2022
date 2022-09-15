#!/usr/bin/env python3

from re import *

dh = globals()
d = {}

err_regex = compile(r'/{2,}|\*\*|[0-9A-Za-z]\w*\(|\.|([^0-9A-Za-z_](\d)+[eE][+-]\d)')
subst_regex = compile(r"(?<!\w)([A-Za-z_]\w*)")
name_regx =  compile(r"([A-Za-z_]\w*)\s*=\s*(.*)")

def analyze(inpt):
  if match(r"#", inpt) is None:

    if err_regex.search(inpt):
      print("Syntax error")
      return

    inpt = sub(r"/", r"//", inpt)
    inpt = subst_regex.sub(r"_c_\1", inpt)

    if subst_regex.fullmatch(inpt):
      try:
        print(eval(inpt, dh, d))

      except NameError:
        print("Name error")
        return

      else:
        return

    elif name_regx.match(inpt):
      s = name_regx.match(inpt)
      left = s.group(1)
      right = s.group(2)

      try:
        right = eval(right, dh, d)

      except NameError:
        print("Name error")
        return

      except SyntaxError:
        print("Syntax error")

      else:
        try:
          exec(left + "=" + str(right), dh, d)

        except SyntaxError:
          print("Syntax error")
          return

        else:
          return

    else:
      if search(r"=", inpt):
        print("Assignment error")
        return

      try:
        print(eval(inpt, dh, d))

      except NameError:
        print("Name error")
        return

      except SyntaxError:
        print("Syntax error")
        return

      except:
        print("Runtime error")
        return

      else:
        return

a = input()
while a:
  analyze(a)
  a = input()

# EOF