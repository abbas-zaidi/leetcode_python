# Write a function to find the length of the longest substring containing the same 
# letter in a given string s, after performing at most k operations in which you 
# can choose any character of the string and change it to any other uppercase English letter.

# Input:

# s = "BBABCCDD"
# k = 2
# Output:5
# Explanation: Replace the first 'A' and 'C' with 'B' to form "BBBBBCDD". 
# The longest substring with identical letters is "BBBBB", which has a length of 5.

def long_repeated(s:str,k:int):

    state = {}
    start = 0
    max_freq = 0
    max_len = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end],0)+1
        max_freq = max(max_freq,state[s[end]])

        if k+max_freq < end - start +1:
            state[s[start]]-=1
            start+=1

        max_len = max(max_len,end-start+1)
    
    return max_len


print("max_len = ",long_repeated("BBABCCDD",2))