#!/usr/bin/env python3

import tarfile
import io 
import sys

hexdump = sys.stdin.read()
hexdump = bytearray.fromhex(hexdump)

tf = tarfile.open(fileobj=io.BytesIO(hexdump))

fcounter = 0
tsize = 0

for fi in tf.getmembers():
	if fi.isfile():
		fcounter += 1
		tsize += fi.size

tf.close()
print(tsize, fcounter)

# EOF