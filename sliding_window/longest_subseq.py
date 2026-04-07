# Write a function to return the length of the longest substring in a provided string s 
# where all characters in the substring are distinct.

# Example 1: Input:

# s = "eghghhgg"
# Output: 3

def long_subseq(s:str):
    state = {}
    start = 0
    max_len = 0

    for end,_ in enumerate(s):
        state[s[end]]=state.get(s[end],0)+1

        while state[s[end]]>1:
            state[s[end]] = state[s[end]] - 1
            if state[s[end]] == 0:
                del state[s[end]]
            start+=1
        max_len = max(max_len,end-start+1)

    return max_len
            
print("Output = ",long_subseq("eghghhgg"))
print("Output = ",long_subseq("substring"))

