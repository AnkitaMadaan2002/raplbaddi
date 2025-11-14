# Copyright (c) 2025, Nishant Bhickta and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OperationEntryItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_qty_produced: DF.Float
		item_code: DF.Link | None
		item_name: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		qty__100_level: DF.Float
		qty__80_level: DF.Float
		qty_as_per_cycle_time: DF.Float
		remarks: DF.SmallText | None
	# end: auto-generated types
	pass
