import csv
from collections import Counter


def read_csv(path_to_file):
    try:
        with open(path_to_file, "r") as file:
            csv_file = csv.reader(file)
            return list(csv_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


# teste = read_csv("data/orders_1.csv")


def favorite(name, orders):
    name_orders = [order[1] for order in orders if order[0] == name]
    return Counter(name_orders).most_common()[0][0]


# print(favorite("maria", teste))


def ordered_food(name, food, orders):
    qnt = 0
    for order in orders:
        if order[0] == name and order[1] == food:
            qnt += 1
    return qnt


# print(ordered_food("arnaldo", "hamburguer", teste))


def never_ordered(name, orders):
    food = set()
    client_food = set()

    for order in orders:
        food.add(order[1])

    for order in orders:
        if order[0] == name:
            client_food.add(order[1])

    return food.difference(client_food)


# print(never_ordered("joao", teste))


def never_visited(name, orders):
    days = set()
    client_days = set()

    for order in orders:
        days.add(order[2])

    for order in orders:
        if order[0] == name:
            client_days.add(order[2])

    return days.difference(client_days)


# print(never_visited("joao", teste))


def analyze_log(path_to_file):
    if (path_to_file.endswith('.csv')):
        orders = read_csv(path_to_file)

        favorite_food = favorite("maria", orders)

        arnaldo_ordered_hamburguer = ordered_food(
            "arnaldo", "hamburguer", orders
        )

        never_ordered_by_joao = never_ordered("joao", orders)

        never_visited_by_joao = never_visited("joao", orders)

        answers = (
            f"{favorite_food}\n{arnaldo_ordered_hamburguer}\n"
            f"{never_ordered_by_joao}\n{never_visited_by_joao}"
        )

        with open("data/mkt_campaign.txt", "w") as file:
            file.writelines(answers)
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
