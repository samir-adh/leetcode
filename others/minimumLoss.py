def minimumLoss(price):
    # Write your code here
    min_loss = -1e17
    buy = 0
    sell = 1
    n = len(price)
    while sell < n:
        if price[buy] > price[sell]:
            loss = price[sell] - price[buy]
            if loss < 0:
                min_loss = max(min_loss, loss)
            buy = sell
            sell += 1
        else :
            sell += 1
    return min_loss

price = [20,15,8,2,12]
print(minimumLoss(price))
