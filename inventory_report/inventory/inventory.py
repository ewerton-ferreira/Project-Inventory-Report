import csv
import json
import xmltodict
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
# https://pypi.org/project/xmltodict/
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

    def json_imported(path):
        with open(path) as file:
            data = json.load(file)
        return data

    def xml_imported(path):
        with open(path, 'r') as file:
            data = xmltodict.parse(file.read())['dataset']['record']
        return data

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith('.csv'):
            data = Inventory.csv_imported(path)
        if path.endswith('.json'):
            data = Inventory.json_imported(path)
        if path.endswith('.xml'):
            data = Inventory.xml_imported(path)
        if type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
