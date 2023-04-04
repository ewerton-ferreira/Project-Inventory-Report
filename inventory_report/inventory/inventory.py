import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def csv_imported(path):
        data = []
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith('.csv'):
            data = Inventory.csv_imported(path)

        if type == "simples":
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError("O tipo de relatório é inválido")
