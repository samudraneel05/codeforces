t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    smallest = a[0]

    second_smallest = None
    for num in a[1:]:
        if num % smallest != 0:
            second_smallest = num
            break

    if second_smallest is None:
        second_smallest = smallest


    is_beautiful = True
    for num in a:
        if num % smallest != 0 and num % second_smallest != 0:
            is_beautiful = False
            break


    if is_beautiful:
        print("Yes")
    else:
        print("No")
