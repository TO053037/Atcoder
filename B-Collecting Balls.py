N = int(input())
K = int(input())
x = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans += 2 * min(x[i], K - x[i])
print(ans)
    