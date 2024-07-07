t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    
    xor_values = []
    
    # Calculate all XOR values for subarrays of length >= 2
    for i in range(n):
        current_xor = 0
        for j in range(i + 1, n):
            current_xor ^= a[j]
            xor_values.append(current_xor)
    
    # Sort the XOR values
    xor_values.sort()
    
    # Print the k-th smallest element directly
    print(xor_values[k - 1])