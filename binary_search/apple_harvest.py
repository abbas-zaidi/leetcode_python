def time_taken(rate):
        time = 0
        for i in range(len(apples)):
            # print("(apples[i] + rate - 1) = ",(apples[i] + rate - 1))
            # time += (apples[i] + rate - 1) // rate
            # print("time = ",time)
            time+=-(-apples[i]//rate)
            # print("time = ",time)           
        return time

def min_rate_brute_force(apples, h):
    rate = 1
    # return time_taken(rate)
    while time_taken(rate) > h:
        rate += 1
    return rate

def min_rate_bsearch(apples,h):
    left,right=0,max(apples)

    while left < right:
        mid = (left+right) //2

        if time_taken(mid)>h:
              left=mid+1
        else:
             right = mid
    return left        



apples = [4, 7, 9, 12]
h = 6
print(min_rate_brute_force(apples,h))
print(min_rate_bsearch(apples,h))