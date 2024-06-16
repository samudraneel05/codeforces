def functionsamp(nums, queries):
    n = len(nums)
    answer = []
    for query in queries:
        if query[0] == 2:
            nums[query[1]] = query[2]
        if query[0] == 1:
            count = 0 
            for i in range(query[1]+1, query[2]):
                if nums[i-1] < nums[i] > nums[i+1]:
                    count += 1
            answer.append(count)
    return answer