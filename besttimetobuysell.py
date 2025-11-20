
def maxProf(prices)->int:
    min = prices[0]
    profit = 0

    for i in range(len(prices)):
        if prices[i]<min:
            min = prices[i]
        profit = max(profit,prices[i]-min)

    return profit


prices_ = [7,1,3,5,9,3,0]

print(maxProf(prices_))