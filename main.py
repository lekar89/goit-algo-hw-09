from faker import Faker
import timeit


SET_OF_COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    check_amount(amount)

    result = {}
    remaining_amount = amount

    for coin in SET_OF_COINS:
        if remaining_amount >= coin:
            num_coins = remaining_amount // coin
            result[coin] = num_coins
            remaining_amount %= coin

    return result


def find_min_coins(amount):
    check_amount(amount)
    remaining_amount = amount

    dp_table = [float("inf")] * (amount + 1)
    dp_table[0] = 0

    coin_used = [-1] * (amount + 1)

    for coin in SET_OF_COINS:
        for i in range(coin, amount + 1):
            if dp_table[i - coin] + 1 < dp_table[i]:
                dp_table[i] = dp_table[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coin_used[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin

    return result


def check_amount(amount):
    if amount == 0 or min(SET_OF_COINS) > amount:
        return {}


def generate_random_amount(min, max):
    fake = Faker()
    return fake.random_int(min=min, max=max)


def measurement(amount):
    greedy = timeit.timeit(lambda: print(find_coins_greedy(amount)), number=1)
    print(f"A greedy algorithm function: {greedy}")
    min = timeit.timeit(lambda: print(find_min_coins(amount)), number=1)
    print(f"Dynamic programming function: {min}")


amount = generate_random_amount(500001 , 10000001)
print(f"Amount: {amount}")
measurement(amount)
