def solve(a, b, c, total):
    flag = [False] * 3
    n = len(a)
    ans = [0] * 6
    j = 0
    sum_val = 0
    ans[0] = 1
    for j in range(n):
        sum_val += a[j]
        ans[1] = j + 1
        if sum_val >= (total + 2) // 3:
            j += 1
            flag[0] = True
            break
    sum_val = 0
    ans[2] = j + 1
    for j in range(j, n):
        sum_val += b[j]
        ans[3] = j + 1
        if sum_val >= (total + 2) // 3:
            j += 1
            flag[1] = True
            break
    sum_val = 0
    ans[4] = j + 1
    for j in range(j, n):
        sum_val += c[j]
        ans[5] = j + 1
        if sum_val >= (total + 2) // 3:
            j += 1
            flag[2] = True
            break
    return all(flag), ans

def solve_case():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + n]))
        index += n
        c = list(map(int, data[index:index + n]))
        index += n
        
        total = sum(a)
        found = False
        for i in range(6):
            aa, bb, cc = a[:], b[:], c[:]
            if i == 0:
                flag, ans = solve(aa, bb, cc, total)
            elif i == 1:
                flag, ans = solve(aa, cc, bb, total)
            elif i == 2:
                flag, ans = solve(bb, aa, cc, total)
            elif i == 3:
                flag, ans = solve(bb, cc, aa, total)
            elif i == 4:
                flag, ans = solve(cc, aa, bb, total)
            elif i == 5:
                flag, ans = solve(cc, bb, aa, total)
            
            if flag:
                ans[5] = n
                if i == 0:
                    results.append(f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]} {ans[5]}")
                elif i == 1:
                    results.append(f"{ans[0]} {ans[1]} {ans[4]} {ans[5]} {ans[2]} {ans[3]}")
                elif i == 2:
                    results.append(f"{ans[2]} {ans[3]} {ans[0]} {ans[1]} {ans[4]} {ans[5]}")
                elif i == 3:
                    results.append(f"{ans[4]} {ans[5]} {ans[0]} {ans[1]} {ans[2]} {ans[3]}")
                elif i == 4:
                    results.append(f"{ans[2]} {ans[3]} {ans[4]} {ans[5]} {ans[0]} {ans[1]}")
                elif i == 5:
                    results.append(f"{ans[4]} {ans[5]} {ans[2]} {ans[3]} {ans[0]} {ans[1]}")
                found = True
                break
        
        if not found:
            results.append("-1")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve_case()