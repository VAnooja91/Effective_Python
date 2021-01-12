import csv


def parse_csv(filename):
    with open(filename) as fh:
        rows = csv.reader(fh)

        headers = next(rows)
        records = []

        for row in rows:
            if not row:
                continue
            data = dict(zip(headers, row))
            records.append(data)

    return records



