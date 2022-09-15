#!/usr/bin/env python3

import base64

s = input()
# s = "1pod3sdqp1V;v|??MM2idn8p=)rm(+um"

a = base64.b85decode(s)

sizes = []

for byte in a[0:a.find(b'\x00')]:
	sizes.append(int.from_bytes([byte], byteorder='big', signed=True))

body = a[a.find(b'\x00')+1:]
tsum = 0
r_size = sum(map(abs, sizes))

for i in range(len(body) // r_size):
	ptr = i * r_size
	offset = 0
	for sz in sizes:
		tsum += int.from_bytes(body[ptr+offset:ptr+offset+abs(sz)], byteorder='big', signed=True if sz < 0 else False)
		offset += abs(sz)

print(tsum)
# assert(tsum == 5599084740)

# EOF