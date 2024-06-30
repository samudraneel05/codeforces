t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    cakes = list(map(int, input().strip().split()))
    
    cakes.sort()
    
    alice_cakes = []
    bob_cakes = []
    
    for i in range(n):
        if i % 2 == 0:
            if len(alice_cakes) == 0 or cakes[i] > alice_cakes[-1]:
                alice_cakes.append(cakes[i])
            else:
                break
        else:
            if cakes.count(cakes[i]) == 1:
                bob_cakes.append(cakes[i])
            else:
                while cakes.count(cakes[i])!= 1:
                    i
    print(len(alice_cakes))
