class Inventory:

    def __init__(self, products):
        self._products = products

    def __iter__(self):
        return self._products.__iter__()

    @property
    def total_cost(self):
        return sum([p.cost for p in self._products])

    def total_quant(self):
        from collections import Counter
        total_units = Counter()
        for p in self._products:
            total_units[p.name] += p.quant
        return total_units
