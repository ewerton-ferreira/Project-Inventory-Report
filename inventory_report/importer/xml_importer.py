import xmltodict
from inventory_report.importer.importer import Importer
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
# https://pypi.org/project/xmltodict/


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError("Arquivo inválido")
        with open(path, 'r') as file:
            return xmltodict.parse(file.read())['dataset']['record']
