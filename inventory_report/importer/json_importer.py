import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        return cls.json_reader(path)

    @classmethod
    def json_reader(cls, path):
        with open(path) as file:
            data = json.load(file)
        return data
