t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    count = 0
    if k != 0:
        if (k - n) <= 0:
            count += 1
        else:
            k -= n
            count += 1
            n -= 1
            while k > 0:
                count += 1
                k -= n
                if k > 0:
                    count += 1
                    k -= n
                n -= 1
    print(count)
        
