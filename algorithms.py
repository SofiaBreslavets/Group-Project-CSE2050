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

def quick_sort(products, maybe_products=None):
    if maybe_products is not None:
        products = maybe_products
    if len(products) <= 1:
        return products
    pivot = products[len(products) // 2]
    left = [x for x in products if x.product_id < pivot.product_id]
    middle = [x for x in products if x.product_id == pivot.product_id]
    right = [x for x in products if x.product_id > pivot.product_id]
    products[:] = quick_sort(left) + middle + quick_sort(right)
    return products

def merge_sort(products, maybe_products=None):
    if maybe_products is not None:
        products = maybe_products
    if len(products) <= 1:
        return products
    midpoint = len(products) // 2
    left = merge_sort(products[:midpoint])
    right = merge_sort(products[midpoint:])
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].product_id <= right[right_index].product_id:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    products[:] = merged
    return products

def quick_select(products, k, maybe_k=None):
    if maybe_k is not None:
        products, k = k, maybe_k
    products = list(products)  # Create a copy to avoid modifying the original list
    if k < 1 or k > len(products):
        return None
    target_index = k - 1
    low = 0
    high = len(products) - 1

    while low <= high:
        pivot_id = products[(low + high) // 2].product_id
        lower = low
        current = low
        upper = high

        while current <= upper:
            product_id = products[current].product_id
            if product_id < pivot_id:
                products[lower], products[current] = products[current], products[lower]
                lower += 1
                current += 1
            elif product_id > pivot_id:
                products[current], products[upper] = products[upper], products[current]
                upper -= 1
            else:
                current += 1

        if target_index < lower:
            high = lower - 1
        elif target_index > upper:
            low = upper + 1
        else:
            return products[target_index]
