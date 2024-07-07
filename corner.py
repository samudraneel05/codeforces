t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr1 = []
    arr2 = []
    
    for _ in range(n):
        s = input().strip()
        row = [int(char) for char in s]
        arr1.append(row)
    
    for _ in range(n):
        s = input().strip()
        row = [int(char) for char in s]
        arr2.append(row)
    
    flag = True
    for i in range(n):
        for j in range(m):
            if arr1[i][j] == arr2[i][j]:
                continue
            
            val = arr1[i][j]
            if i + 1 < n and j + 1 < m:
                if (val + 2) % 3 == arr2[i][j]:
                    arr1[i + 1][j + 1] = (arr1[i + 1][j + 1] + 2) % 3
                    arr1[i][j + 1] = (arr1[i][j + 1] + 1) % 3
                    arr1[i + 1][j] = (arr1[i + 1][j] + 1) % 3
                    arr1[i][j] = arr2[i][j]
                elif (val + 1) % 3 == arr2[i][j]:
                    arr1[i + 1][j + 1] = (arr1[i + 1][j + 1] + 1) % 3
                    arr1[i][j + 1] = (arr1[i][j + 1] + 2) % 3
                    arr1[i + 1][j] = (arr1[i + 1][j] + 2) % 3
                    arr1[i][j] = arr2[i][j]
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        print("YES")
    else:
        print("NO")
