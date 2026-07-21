def perrin(m = 100):
    a, b, c = 3, 0, 2
    results = []
    while a < m:
        results.append(a)
        a, b, c = b, c, a + b
    return results

print(perrin(100))

# p_list = perrin(100000)
p_list = perrin(100)
x_list = list()
for p, n in enumerate(p_list):
    if n == 0:
        continue
    print((n, p), end = ' ')
    if p % n == 0:
        x_list.append(n)

print(x_list)
"""実行結果
[3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, 68, 90]
(3, 0) (2, 2) (3, 3) (2, 4) (5, 5) (5, 6) (7, 7) (10, 8) (12, 9) (17, 10) (22, 11) (29, 12) (39, 13) (51, 14) (68, 15) (90, 16) [3, 2, 3, 2, 5, 7]
"""
