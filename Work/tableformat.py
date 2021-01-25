class TableFormatter:
    def headings(self, headers):
        '''Emit table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit single row of data.
        :param rowdata:
        :return:
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f'{data:10s}', end=' ')
        print()

