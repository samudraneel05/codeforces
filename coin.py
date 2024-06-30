t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    temp1 = 0
    temp2 = 0
    for i in range(n):
        ans += max(0, temp1 - a[i])
        temp2 = max(temp2, temp1-a[i])
        temp1 = max(temp1, a[i])
    ans += temp2
    print(ans)