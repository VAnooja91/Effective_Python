import csv


def read_inventory(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        headers = next(rows)
        invent = list()

        for row in rows:
            name = str(row[0])
            quant = int(row[1])
            price = float(row[2])
            product = {"name": name, "quant": quant, "price": price}
            invent.append(product)

        return invent


def read_prices(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        product = dict()

        for row in rows:
            try:
                product[row[0]] = float(row[1])
            except IndexError:
                continue

        return product


inventory = read_inventory("Data/inventory.csv")
latest_prices = read_prices("Data/prices.csv")

total_cost = 0.0
present_cost = 0.0

for prod in inventory:
    total_cost += prod["quant"] * prod["price"]
    present_cost += prod["quant"] * latest_prices[prod["name"]]

print("total price is: ", total_cost)
print("present value is: ", present_cost)
print("total Gain is: ", present_cost - total_cost)



