import matplotlib.pyplot as plt
from matplotlib.figure import Figure

MIN_NUMBER_OF_ROLL = 10

def get_bw_total_rates(base_nb_roll: int, base_wish_boost: float, is_star_wish: bool) -> list[float]:
    # constant for the base probability to roll a given waifu/husbando
    c = 1
    wish_boost = base_wish_boost
    nb_roll = base_nb_roll
    values: list[float] = []
    for i in range(base_nb_roll - MIN_NUMBER_OF_ROLL + 1):
        rate_by_roll = c * 100 + c * wish_boost
        total_rate = nb_roll * rate_by_roll

        values.append(total_rate)

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
    return values

def show_graph(base_nb_roll: int, base_wish_boost: float, base_starwish_boost: float):
    wish_values = get_bw_total_rates(base_nb_roll, base_wish_boost, False)
    starwish_values = get_bw_total_rates(base_nb_roll, base_starwish_boost, True)
    x = [i for i in range(len(wish_values))]
    plt.plot(x, wish_values, label = "wish_values")
    plt.plot(x, starwish_values, label = "starwish_values")
    plt.legend()
    plt.show()

show_graph(14, 150, 250)
