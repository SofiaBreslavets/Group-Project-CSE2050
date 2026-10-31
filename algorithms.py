def recursive_total_price(products):
    if not products:
        return 0
    return products[0].price + recursive_total_price(products[1:])

def fewest_coins(coins, amount):
    if amount < 0:
        return []
    if any(coin <= 0 for coin in coins):
        raise ValueError("Coin values must be positive")

    min_counts = [float('inf')] * (amount + 1)
    last_coin = [None] * (amount + 1)
    min_counts[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount and min_counts[current_amount - coin] + 1 < min_counts[current_amount]:
                min_counts[current_amount] = min_counts[current_amount - coin] + 1
                last_coin[current_amount] = coin

    if last_coin[amount] is None and amount != 0:
        return []

    result = []
    while amount > 0:
        coin = last_coin[amount]
        result.append(coin)
        amount -= coin
    return result[::-1]


def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j].product_id > products[j+1].product_id:
                products[j], products[j+1] = products[j+1], products[j]
    return products

def insertion_sort(products):
    n = len(products)
    for i in range(1, n):
        key = products[i]
        j = i - 1
        while j >= 0 and key.product_id < products[j].product_id:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    return products

def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if products[j].product_id < products[min_idx].product_id:
                min_idx = j
        products[i], products[min_idx] = products[min_idx], products[i]
    return products

def binary_search(products, product_id):
    left, right = 0, len(products) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if products[mid].product_id == product_id:
            return products[mid]
        elif products[mid].product_id < product_id:
            left = mid + 1
        else:
            right = mid - 1
    return None
