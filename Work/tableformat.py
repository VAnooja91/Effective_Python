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
