S = input()
x = S.count('0')
y = S.count('1')

ans = 2 * (min(x, y))
print(ans)