t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().strip().split())
    if k > (n + 1) * n // 2:
        print("No")
    else:
        if k % 2 != 0:
            print('No')
        else:
            permutation = list(range(1, n + 1))
            print("Yes")
            print(permutation)



# t = int(input().strip())

# # Process each test case
# for _ in range(t):
#     # Read n and k for the current test case
#     n, k = map(int, input().strip().split())
    
#     # Check if k is valid based on maximum possible Manhattan value
#     max_manhattan = (n - 1) * n // 2
#     if k > max_manhattan:
#         print("No")
#         continue
    
#     # Initialize the permutation as [1, 2, ..., n]
#     permutation = list(range(1, n + 1))
    
#     # Adjust permutation to achieve Manhattan value k
#     for i in range(n - 1):
#         if k <= 0:
#             break
        
#         # Calculate the maximum possible increase at position i
#         max_increase = min(k, abs(permutation[i] - (i + 1)))
        
#         # Swap elements to increase the Manhattan value
#         if max_increase > 0:
#             permutation[i], permutation[i + max_increase] = permutation[i + max_increase], permutation[i]
#             k -= max_increase
    
#     # Output result for the current test case
#     if k == 0:
#         print("Yes")
#         print(" ".join(map(str, permutation)))
#     else:
#         print("No")