# Copyright (c) 2023, Athletic Classic and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class CatalogShare(Document):
    @frappe.whitelist()
    def get_catalog_file_list_to_share(self):
        catalog_file_list = []
        file_extension = ".pdf"
        for items in self.select_items:
            catalog_file_list.append(items.items + file_extension )

        return catalog_file_list
