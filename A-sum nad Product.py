S, P = map(int,input().split())
for i in range(1, 10 ** 6 + 1):
    if i * (S - i) == P:
        print('Yes')
        exit()
print('No')

