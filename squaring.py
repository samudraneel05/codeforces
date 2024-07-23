t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    

    acts = 0
    impossible = False
    
    for i in range(1, n):
        while a[i] < a[i-1]:
            a[i] *= a[i]
            acts += 1
            if a[i] < a[i-1] and a[i]==1:
                impossible = True
                break
        if impossible:
            break
    
    if impossible:
        print(-1)
    else:
        print(acts)