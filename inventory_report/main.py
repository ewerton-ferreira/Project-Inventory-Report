from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

report_types = {"simples": SimpleReport, "completo": CompleteReport}


def main():
    try:
        _, file, type = sys.argv

        if ".csv" in file:
            content = InventoryRefactor(CsvImporter)
        elif ".json" in file:
            content = InventoryRefactor(JsonImporter)
        else:
            content = InventoryRefactor(XmlImporter)

        content.import_data(file, type)

        sys.stdout.write(report_types[type].generate(content.data))

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
