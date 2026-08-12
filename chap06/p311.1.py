data = 'golf'
l = [data[i] for i in range(len(data)-1, -1, -1)]
print(l)

g = (data[i] for i in range(len(data)-1, -1, -1))
print(g)
print(list(g))
