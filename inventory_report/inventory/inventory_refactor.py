from typing import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    data = []

    def __init__(self, Importer):
        self.importer = Importer()
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)
