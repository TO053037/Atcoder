n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
x = 0

for i in range(n):
    if a[i] != n:
        x += b[a[i] - 1]
        if i != n -1:
            if a[i + 1] == a[i] + 1:
                x += c[a[i] - 1]
        
    else:
        x += b[a[i] - 1]


print(x)
    