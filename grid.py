from math import ceil

def min_screens(x, y):
    S1 = ceil(y / 2)
    R = S1 * 15 - 4 * y
    x_remaining = x - R
    S2 = ceil(x_remaining / 15) if x_remaining > 0 else 0
    total_screens = S1 + S2
    return total_screens


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min_screens(x, y))