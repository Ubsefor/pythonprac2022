#!/usr/bin/env python3

from fractions import Fraction
import re

s = input()

a = re.sub('(\d+(?:\.\d*)?|\.\d+)', lambda x: repr(Fraction (x.group())), s)

print(Fraction(eval(a)))

#EOF