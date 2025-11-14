# Copyright (c) 2025, Nishant Bhickta and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)

    return columns, data 
def get_columns():
    return [
        {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 200},
        {"label": _("Brand"), "fieldname": "brand", "fieldtype": "Link", "options": "Brand", "width": 150},
        {"label": _("Item Code"), "fieldname": "item_code", "fieldtype": "Link", "options": "item", "width": 150},
        {"label": _("Item Group"), "fieldname": "item_group", "fieldtype": "Link","options": "Item Group", "width": 150},
        {"label": _("Total Quantity"), "fieldname": "total_qty", "fieldtype": "Int", "width": 120},
        {"label": _("Freight Amount"), "fieldname": "freight_amount", "fieldtype": "Currency", "width": 150},
        
    ]


def get_data(filters):
    conditions = "1 = 1"
    
    if filters.get("from_date") and filters.get("to_date"):
        conditions += " AND dn.posting_date BETWEEN %(from_date)s AND %(to_date)s"
    if filters.get("customer"):
        conditions +=  " AND dn.customer = %(customer)s"
    if filters.get("brand"):
        conditions += " AND dni.brand = %(brand)s"
    if filters.get("item_code"):
        conditions += " AND dni.item_code = %(item_code)s"
    if filters.get("item_group"):
        conditions += " AND i.item_group = %(item_group)s"
    if filters.get("status"):
        if filters["status"] == "Draft":
            conditions += " AND dn.docstatus = 0"
        elif filters["status"] == "Submitted":
            conditions += " AND dn.docstatus = 1"
        elif filters["status"] == "Cancelled":
            conditions += " AND dn.docstatus = 2"
        elif filters["status"] == "to Bill":
            conditions += " AND dn.docstatus = 3"
        

    query = f"""
        SELECT
            dn.customer,
            dn.customer_name,
            IFNULL(NULLIF(dni.brand, ''), 'No Brand') AS brand,
            dni.item_code,
            i.item_group,
            SUM(dni.qty) AS total_qty,
            SUM(dn.amount) AS freight_amount
        FROM 
            `tabDelivery Note Item` dni
        JOIN 
            `tabDelivery Note` dn ON dn.name = dni.parent
        JOIN 
            `tabItem` i ON i.name = dni.item_code
        WHERE 
            {conditions}
        GROUP BY 
            dni.item_code, dn.customer

    """

    return frappe.db.sql(query, filters, as_dict=True)