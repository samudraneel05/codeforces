def max_pages(n, pages):
    max_other_pages = max(pages[:-1])
    max_pages = pages[-1] + max_other_pages
    
    return max_pages

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    pages = list(map(int, input().strip().split()))
    result = max_pages(n, pages)
    print(result)