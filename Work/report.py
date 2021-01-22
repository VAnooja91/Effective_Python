import csv
from fileparse import parse_csv
from product import Product


def read_inventory(filename):
    with open(filename) as FH:
        invent = parse_csv(FH, select=['name', 'quant', 'price'], types=[str, int, float])
        prodinv = [Product(p['name'], p['quant'], p['price']) for p in invent]
    return prodinv


def read_prices(filename):
    with open(filename) as FH:
        pricelist = parse_csv(FH, types=[str, float], has_headers=False)
        product = dict(pricelist)
    return product


def make_report(product, prices):
    values = list()

    for prod in product:
        name = prod.name
        quant = prod.quant
        price = prod.price
        latest_price = prices[name]
        values.append((name, quant, latest_price,latest_price-price))

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


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage:{argv[0]} ''inventory latest_prices')
    inventory = argv[1]
    latest_prices = argv[2]
    inventory_report(inventory, latest_prices)


if __name__ == "__main__":
    import sys
    main(sys.argv)

