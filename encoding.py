t = int(input()) 

for _ in range(t):
    n = int(input())  
    b = input()  
    r = ''.join(sorted(set(b)))  
    s = ''.join(r[-(r.index(c)+1)] for c in b)
    print(s)
