# TLE
t = int(input())  

for _ in range(t):
    n = int(input()) 
    h = list(map(int, input().split()))  

    seconds = 0

    while any(height > 0 for height in h): 
        for i in range(n):
            if i == n - 1 or h[i] > h[i + 1]:
                h[i] = max(0, h[i] - 1)
        seconds += 1

    print(seconds)


# Optimal

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split())) 
    ans = 0
    for i in range(n):
        ans = max(ans, h[i] + i)
    
    print(ans)