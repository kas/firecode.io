# 3.1 Stock Market Oracle

def max_profit(prices):
    prices_length = len(prices)

    profit = 0

    for i in range(0, prices_length, 2):
        if i == prices_length - 1:
            break

        current_profit = prices[i + 1] - prices[i]

        if current_profit < 0:
            continue

        profit += current_profit

    return profit
