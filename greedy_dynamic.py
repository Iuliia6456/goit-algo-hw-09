import timeit

denomination = [50, 25, 10, 5, 1]

def find_coins_greedy(amount):
    dict_result = {}
    for coin in denomination:
        coins_used = amount // coin
        if coins_used > 0:
            dict_result[coin] = coins_used
            amount = amount % coin
     
    return dict_result

def find_min_coins(amount):
    
    min_coins_required = [0] + [float("inf")] * amount 
    last_coin_used = [0] * (amount + 1) 

    for s in range(1, amount + 1):
        for coin in denomination:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin
    
    count_coins = {}
    current_sum = amount
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin

    return count_coins

def comparison(amount):
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=10)
    time_dynamic = timeit.timeit(lambda: find_min_coins(amount), number=10)
    return time_greedy, time_dynamic


if __name__ == '__main__':
    
    amount = 1513
    greedy_time, dynamic_time = comparison(amount)
    print(f"\nGreedy algorithm ---> {amount} UAH can be given as {find_coins_greedy(amount)} coins")
    print(f"Greedy time: {greedy_time:.6f} sec\n")
    
    print(f"Dynamic algorithm ---> {amount} UAH can be given as {find_min_coins(amount)} coins")
    print(f"Dynamic time: {dynamic_time:.6f} sec\n")
    