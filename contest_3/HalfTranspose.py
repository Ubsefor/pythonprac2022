mat = list()
res = []

inp = input().split(',')

for i in range(0, len(inp) - 1):
  mat.append(inp)
  inp = input().split(',')

mat.append(inp)

# print(mat)

print (mat[0][0])

for i in range(1, len(mat)):

	for j in range(0, i):
		res.append(mat[i][j])

	res.append(mat[i][i])

	for k in range(i-1 , 0, -1):
		res.append(mat[k][i])

	res.append(mat[0][i])

	print(','.join(res))
	res = []
