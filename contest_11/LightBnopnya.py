#!/usr/bin/env python3

import sys

encodings = "cp037 cp1006 cp1250 cp1251 cp1253 cp1254 cp1255 cp1256 cp1257 cp1258 cp437 cp720 cp737 cp775 cp850 cp852 cp855 cp864 cp866 cp869 cp874 cp875 hp_roman8 iso8859_10 iso8859_16 iso8859_4 iso8859_5 koi8_r latin_1 mac_croatian mac_greek mac_iceland mac_latin2".split(" ")

inp = sys.stdin.read().strip()

def check_enc(byts):
  s = byts.decode('koi8_r')
  if not (s.startswith('ПРОЦ') and s.endswith('КНЦ;') and s.find('ВЫВОД:')):
    return False
  for c in s:
    if c.isalpha():
      if not ('А' <= c <= 'Я' or c == 'Ё'):
        return False
  return True

for enc_1 in encodings:
  try:
    tmp1 = inp.encode(enc_1)
  except UnicodeError:
    continue

  for enc_2 in encodings:
    try:
      tmp2 = tmp1.decode(enc_2)
    except UnicodeError:
      continue

    for enc_3 in encodings:
      try:
        tmp3 = tmp2.encode(enc_3)
      except UnicodeError:
        continue

      for enc_4 in encodings:
        try:
          tmp4 = tmp3.decode(enc_4)
        except UnicodeError:
          continue

        for enc_5 in encodings:
          try:
            tmp5 = tmp4.encode(enc_5)
            # print(tmp5.decode('koi8_r'))
            if check_enc(tmp5):
              print(inp.encode(enc_1)
                        .decode(enc_2)
                        .encode(enc_3)
                        .decode(enc_4)
                        .encode(enc_5)
                        .decode('koi8_r'))
              sys.exit(0)
          except UnicodeError:
            continue


# EOF