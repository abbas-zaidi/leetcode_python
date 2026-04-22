# DESCRIPTION (inspired by Leetcode.com)
# You are given a sorted array that has been rotated at an unknown pivot point, along with a target value. Develop an algorithm to locate the index of the target value in the array. If the target is not present, return -1. The algorithm should have a time complexity of O(log n).

# Note:

# The array was originally sorted in ascending order before being rotated.
# The rotation could be at any index, including 0 (no rotation).
# You may assume there are no duplicate elements in the array.
# Example 1:
# Input:

# nums = [4,5,6,7,0,1,2], target = 0

def search_rotated_array(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            # left array is sorted
            if target>=nums[left] and target<=nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            # right array is sorted
            if target>=nums[mid] and target<=nums[right]:
                left = mid+1
            else:
                right = mid
    