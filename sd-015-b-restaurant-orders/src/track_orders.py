from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        name_orders = [
            order[1] for order in self.orders if order[0] == customer
        ]
        return Counter(name_orders).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        food = set()
        client_food = set()

        for order in self.orders:
            food.add(order[1])

        for order in self.orders:
            if order[0] == customer:
                client_food.add(order[1])

        return food.difference(client_food)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        client_days = set()

        for order in self.orders:
            days.add(order[2])

        for order in self.orders:
            if order[0] == customer:
                client_days.add(order[2])

        return days.difference(client_days)

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return Counter(days).most_common()[0][0]

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return Counter(days).most_common()[-1][0]
