# Write a function to calculate the maximum number of fruits you can collect from an 
# integer array fruits, where each element represents a type of fruit. 
# You can start collecting fruits from any position in the array, 
# but you must stop once you encounter a third distinct type of fruit. 
# The goal is to find the longest subarray where at most two different types of fruits are collected.

# Example:
# Input: fruits = [3, 3, 2, 1, 2, 1, 0]
# Output: 4
# Explanation: We can pick up 4 fruit from the subarray [2, 1, 2, 1]

def fruits_in_basket(fruits: list[int]):
    state:dict[int,int] = {}
    n = len(fruits)
    start = 0
    count = 0
    if n == 0:
        return 0

    for end in range(n):
        state[fruits[end]] = state.get(fruits[end],0)+1

        while len(state) > 2:
            state[fruits[start]] = state[fruits[start]]-1
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            start+=1
        
        count = max(count,end-start+1) 
    return count


print("count = ",fruits_in_basket([3, 3, 2, 1, 2, 1, 0]))