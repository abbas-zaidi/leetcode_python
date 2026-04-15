# Given an integer array temps representing daily temperatures, write a function to 
# calculate the number of days one has to wait for a warmer temperature after each given day.
#  The function should return an array answer where answer[i] represents the wait time for a warmer 
# day after the ith day. If no warmer day is expected in the future, set answer[i] to 0.

# Inputs:

# temps = [65, 70, 68, 60, 55, 75, 80, 74]
# Output:[1,4,3,2,1,1,0,0]


def warmer_day(nums:list[int]):
    n = len(nums)
    stack:list[int] = []
    result:list[int] = [0]*n

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
                j = stack.pop()
                result[j] = i-j
        stack.append(i)
    return result

print(warmer_day([73,74,75,71,69,72,76,73]))
print(warmer_day([30,60,90]))
    
