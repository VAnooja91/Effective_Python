from fileparse import parse_csv
from product import Product
from tableformat import create_formatter, print_table


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


def print_report(report, formatter):
    formatter.headings(['Name', 'Quantity', 'prices', 'Change'])
    for name, quant, price, change in report:
        rowdata = [name, str(quant), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def inventory_report(inventory, latest_prices, fmt='txt'):
    inv = read_inventory(inventory)
    price = read_prices(latest_prices)
    report = make_report(inv, price)

    formatter = create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage:{argv[0]}''inventory latest_prices formatter')
    inventory = argv[1]
    latest_prices = argv[2]
    formatter = argv[3]
    inventory_report(inventory, latest_prices, formatter)


if __name__ == "__main__":
    import sys
    main(sys.argv)

