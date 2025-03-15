MIN_NUMBER_OF_ROLL = 10

def get_best_bw_value(base_nb_roll: int, base_wish_boost: float, is_star_wish: bool) -> int:
    # constant for the base probability to roll a given waifu/husbando
    c = 1
    wish_boost = base_wish_boost
    nb_roll = base_nb_roll
    best = (-1, -1)
    for i in range(base_nb_roll - MIN_NUMBER_OF_ROLL + 1):
        best_rate, _ = best
        rate_by_roll = c * 100 + c * wish_boost
        total_rate = nb_roll * rate_by_roll

        if total_rate > best_rate:
            best = (total_rate, i)

        nb_roll -= 1

        if i < 5:
            wish_boost += 20
        elif i < 15:
            wish_boost += 15
        elif i < 100:
            wish_boost += 10
        elif i < 200:
            wish_boost += 5
        else:
            wish_boost += 1

        if is_star_wish and i < 100:
            wish_boost += 10
        elif is_star_wish and i < 200:
            wish_boost += 5
        elif is_star_wish:
            wish_boost += 1
    return best[1]


print(get_best_bw_value(13, 150, False))
print(get_best_bw_value(13, 250, True))
