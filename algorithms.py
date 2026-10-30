def recursive_total_price(products):
    if not products:
        return 0
    return products[0].price + recursive_total_price(products[1:])

def fewest_coins(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        res = fewest_coins(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    return min_coins

fewest_coins([1, 5, 10, 25], 63)  # Example usage

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

def insertion_sort(products):
    n = len(products)
    for i in range(1, n):
        key = products[i]
        j = i - 1
        while j >= 0 and key.price < products[j].price:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key

def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if products[j].price < products[min_idx].price:
                min_idx = j
        products[i], products[min_idx] = products[min_idx], products[i]

def binary_search(products, product_id):
    left, right = 0, len(products) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if products[mid].id == product_id:
            return products[mid]
        elif products[mid].id < product_id:
            left = mid + 1
        else:
            right = mid - 1
    return None