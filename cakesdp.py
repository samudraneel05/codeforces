import sys
input = sys.stdin.read
from functools import lru_cache

M = 1000000007
N = 5010
dp = [[-1] * (N + 1) for _ in range(N + 1)]
ct = [0] * (N + 1)

@lru_cache(None)
def r(i, asc):
    if asc < 0:
        return -2
    if i == 0:
        return -2 if asc else 0
    if dp[i][asc] != -1:
        return dp[i][asc]
    dp[i][asc] = r(i - 1, asc - 1) if asc > 0 else r(i - 1, asc)
    if asc >= 0 and r(i - 1, asc - 1) != -2 and r(i - 1, asc - 1) + ct[i] <= asc:
        if dp[i][asc] == -1 or r(i - 1, asc - 1) + ct[i] < dp[i][asc]:
            dp[i][asc] = r(i - 1, asc - 1) + ct[i]
    return dp[i][asc]

for _ in range(int(input())):
    input_data = input().split()
    tc = int(input_data[0])
    n = int(input_data[1])
    ans = n
    for i in range(1, n + 1):
        ct[i] = int(input_data[1 + i])

    for i in range(n, -1, -1):
        if r(n, i) != -2:
            ans = i
            break

    print(ans)