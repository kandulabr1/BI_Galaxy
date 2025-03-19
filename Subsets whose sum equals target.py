def find_subsets(arr, target, index=0, subset=[], result=[]):

    if len(subset) >= 2 and sum(subset) == target:
        result.append(subset[:])
    
    for i in range(index, len(arr)):
        subset.append(arr[i])
        find_subsets(arr, target, i + 1, subset, result)
        subset.pop()
    
    return result

arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))
result = find_subsets(arr, target)
print("Subsets whose sum equals target:", result)