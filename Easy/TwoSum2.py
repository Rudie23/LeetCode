from typing import List

arr1 = [1, 2, 3]
target = 3


def twosum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        if (target - num) in seen:
            return ([seen[target - num], i])
        elif num not in seen:
            seen[num] = i
        print(seen)


list1 = twosum(arr1, target)
print(list1)
