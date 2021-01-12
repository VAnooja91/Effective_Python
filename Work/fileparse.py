import csv


def parse_csv(filename, select=None):
    with open(filename) as fh:
        rows = csv.reader(fh)

        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue

            if indices:
                row = [row[index] for index in indices]
                
            data = dict(zip(headers, row))
            records.append(data)

    return records
