import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")
        return cls.csv_reader(path)

    @classmethod
    def csv_reader(cls, path):
        data = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
