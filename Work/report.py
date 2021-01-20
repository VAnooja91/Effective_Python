import csv
from fileparse import parse_csv


def read_inventory(filename):
    invent = parse_csv(filename, select=['name', 'quant', 'price'], types=[str, int, float])
    return invent


def read_prices(filename):
    pricelist = parse_csv(filename, types=[str, float], has_headers=False)
    product = dict(pricelist)
    return product


def make_report(product, prices):
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


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage:{argv[0]} ''inventory latest_prices')
    inventory = argv[1]
    latest_prices = argv[2]
    inventory_report(inventory, latest_prices)


if __name__ == "__main__":
    import sys
    main(sys.argv)

