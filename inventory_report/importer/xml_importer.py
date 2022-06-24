import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")
        return cls.xml_reader(path)

    @classmethod
    def xml_reader(cls, path):
        with open(path) as file:
            reader = file.read()
            data = xmltodict.parse(reader)
            data = data["dataset"]["record"]
        return data
