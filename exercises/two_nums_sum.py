# gets a list and int x, search if there are 2 numbers in the list that their sum == x
def two_nums(arr, x):    # O(nlogn)
    arr.sort()
    i = 0
    j = len(arr) - 1
    while j > i:
        if arr[i] + arr[j] == x:
            return True
        if arr[i] + arr[j] > x:
            j -= 1
            continue
        else:
            i += 1
            continue


nums = [1, 3, 5, 65, 1, 2, 32, 21, 0, 10]
print two_nums(nums, 34)
