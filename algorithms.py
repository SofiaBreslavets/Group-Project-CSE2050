def recursive_total_price(products):
    if not products:
        return 0
    return products[0].price + recursive_total_price(products[1:])

def fewest_coins(coins, amount):
    if any(coin <= 0 for coin in coins):
        raise ValueError("Coin values must be positive")

    memo = {0: 0}

    def min_coins(remaining):
        if remaining < 0:
            return float('inf')
        if remaining in memo:
            return memo[remaining]

        best = float('inf')
        for coin in coins:
            best = min(best, min_coins(remaining - coin) + 1)
        memo[remaining] = best
        return best

    result = min_coins(amount)
    return -1 if result == float('inf') else result


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
        current_id = getattr(products[mid], "product_id", products[mid])
        if current_id == product_id:
            return mid
        elif current_id < product_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def quick_sort(products):
    pass

def merge_sort(products):
    pass

def quick_select(products, k):
    pass
    
