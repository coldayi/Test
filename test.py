# 快速排序函数
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [32, 5, 67, 567, 37, 678, 45]
print("排序前:", arr)
print("排序后:", quicksort(arr))
