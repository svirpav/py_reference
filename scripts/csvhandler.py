import csv
from scripts import matplot


class CsvHandler:

    def __init__(self):
        self.file = '56_CO_LINES.csv'
        self.mp = matplot.Plot()

    def csvhandler(self):
        col = self.__read_first_row()

        # return index of an Item
        index_created = col.index('Created')
        index_customer = col.index('Customer No')
        index_Sales_qty = col.index('Sales Qty')
        index_sales_part = col.index('Sales Part No')

        data = self.__customer_data()
        data_dict = dict()
        for row in data:
            if 'FLEXTRONICS BRAZIL' in row:
                if row[index_sales_part] not in data_dict:
                    data_dict[row[index_sales_part]] = []
                    data_dict[row[index_sales_part]].append(float(row[index_Sales_qty]))
                else:
                    data_dict[row[index_sales_part]].append(float(row[index_Sales_qty]))
        for item in data_dict:
            data_dict[item] = sum(data_dict[item])

        self.mp.data_plot(data_dict)

    def __dict_read(self):
        pass

    def __simple_read(self):
        pass

    def __read_first_row(self):
        with open(self.file, encoding='unicode-escape', newline='') as f:
            data = csv.reader(f)
            for row in data:
                a = row
                break
        f.close()
        return a

    def __customer_data(self):
        a = []
        with open(self.file, encoding='unicode-escape', newline='') as f:
            data = csv.reader(f)
            for row in data:
                a.append(row)
        f.close()
        return a
