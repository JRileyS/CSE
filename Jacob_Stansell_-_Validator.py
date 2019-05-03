def valid_card_num(num):
    if len(num) == 15:
        num_short = num.remove(15)
        num_rev = num_short[::-1]
        multipliers = [2, 1]


print(valid_card_num([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]))
