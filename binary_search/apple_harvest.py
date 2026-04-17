def min_rate(apples, h):
    def time_taken(rate):
        time = 0
        for i in range(len(apples)):
            # print("(apples[i] + rate - 1) = ",(apples[i] + rate - 1))
            # time += (apples[i] + rate - 1) // rate
            # print("time = ",time)
            time+=-(-apples[i]//rate)
            # print("time = ",time)           
        return time
    rate = 1
    # return time_taken(rate)
    while time_taken(rate) > h:
        rate += 1
    return rate

apples = [25, 9, 23, 8, 3]
h = 5
print(min_rate(apples,h))