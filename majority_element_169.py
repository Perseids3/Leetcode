def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ### How to achieve this in O(1) space while keeping the time complexity to be O(n)?
    ### Boyer-Moore Voting Algorithm:
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

nums = [1,2,3,4,5,6,7,3,2,1,2,3,4,2,2,2,3,2,2,2,2,2]
print(majorityElement(nums))