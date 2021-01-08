import csv


def read_inventory(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)
        header = next(rows)
        invent = list()

        for rowno, row in enumerate(rows, start=1):
            prod = dict(zip(header, row))
            prod['quant'] = int(prod["quant"])
            prod['price'] = float(prod["price"])
            invent.append(prod)

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


def make_report(product,prices):
    values = list()

    for prod in product:
        name = prod['name']
        quant = prod['quant']
        price = prod['price']
        latest_price = prices[name]
        values.append ((name,quant,latest_price,latest_price-price))

    return values


def print_report(report):
    headers = ('Name', 'Quantity', 'prices', 'Change')
    print('%10s %10s %10s %10s' % headers)
    width = 10
    n_cols = len(headers)
    print(f"{'-' * width} " * n_cols)
    for name, quant, price, change in report:
        print(f'{name:>10s}{quant:>10d}{price:10.2f}{change:>10.2f}')


def inventory_report(inventory, latest_prices):
    inv = read_inventory(inventory)
    price = read_prices(latest_prices)
    report = make_report(inv, price)
    print_report(report)


inventory = "Data/inventory.csv"
latest_prices = "Data/prices.csv"

inventory_report(inventory, latest_prices)
