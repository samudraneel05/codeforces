# def calculate_max_profit(n, a, b):
#     max_profit = 0
    
#     for k in range(min(n,b) + 1):
#         profit = sum(b - i for i in range(k)) + (n - k) * a
#         if profit > max_profit:
#             max_profit = profit
    
#     return max_profit

# t = int(input().strip())

# for _ in range(t):
#     n, a, b = map(int, input().strip().split())
#     max_profit = calculate_max_profit(n, a, b)
#     print(max_profit)



t = int(input().strip())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    
    if b < a:
        sum = a * n
    elif b - a >= n:
        sum = (b * (b + 1)) // 2 - ((b - n) * (b - n + 1)) // 2
    else:
        k = b - a + 1
        sum = (b * (b + 1)) // 2 - ((b - k) * (b - k + 1)) // 2 + a * (n - k)
    
    print(sum)