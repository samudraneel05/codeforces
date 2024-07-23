t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().split()))
    a.sort()
    high = 0
    presum = 0
    i = 0 
    for element in a:
        presum += element
        while element - a[i] > 1:
            presum -= a[i]
            i += 1
        while presum > m:
            presum -= a[i]
            i += 1
        high = max(high, presum)
    print(high)
