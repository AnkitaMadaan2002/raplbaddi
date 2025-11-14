# Copyright (c) 2025, Nishant Bhickta and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OperationEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		cycle_time: DF.Float
		date_of_production: DF.Date | None
		depatment: DF.Link | None
		manpower: DF.Int
		remarks: DF.SmallText | None
		shift: DF.Literal[None]
		supervisor_name: DF.Link | None
	# end: auto-generated types
	pass
