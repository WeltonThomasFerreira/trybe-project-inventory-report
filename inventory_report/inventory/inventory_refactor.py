from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer()
        self.data = ''
        self.report_type = ''

    def __iter__(self):
        return InventoryIterator(self.importer, self.data)

    def import_data(self, path, report_type):
        self.data += path
        self.report_type += report_type

