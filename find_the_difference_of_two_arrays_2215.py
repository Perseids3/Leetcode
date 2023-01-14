class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
    ### Well, I can't see there is more convenient way. O(n+m) time complexity seems to be inevitable.
        res = [[],[]]
        for i in nums1:
            if i not in nums2:
                if i not in res[0]:
                    res[0].append(i)
        for k in nums2:
            if k not in nums1:
                if k not in res[1]:
                    res[1].append(k)
        return res
    
    
    
### BEST Way so far:
### return set(nums1)-set(nums2), set(nums2)-set(nums1)