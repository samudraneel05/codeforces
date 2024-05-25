t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[i] != a[j] and a[j] == a[k]) or (a[i] == a[j] and a[j] != a[k]) or (a[i] == a[j] and a[j] == a[k]):
                    count += 1

    print(count)
