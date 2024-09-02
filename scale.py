# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().strip().split())
#     grid = []
#     for i in range(n):
#         grid[i] = map(int, input().strip().split())

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    reduced_size = n // k
    for i in range(reduced_size):
        for j in range(reduced_size):
            block_start_row = i * k
            block_start_col = j * k
            print(grid[block_start_row][block_start_col])
    print()





