# t = int(input().strip())

# for _ in range(t):
#     n = int(input().strip())
#     a = list(map(int, input().strip().split()))
#     b = list(map(int, input().strip().split()))
    
#     if sorted(a) == sorted(b):
#         print("YES")
#     else:
#         print("NO")


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a[:]
    d = b[:]

    c.sort()
    d.sort()

    if c != d:
        print("NO")
        return

    count = 0
    index_map = {value: i for i, value in enumerate(b)}
    for i in range(n):
        if a[i] != b[i]:
            count += 1
            ind = index_map[a[i]]
            b[i], b[ind] = b[ind], b[i]
            index_map[b[ind]] = ind
            index_map[b[i]] = i

    if count % 2 == 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()