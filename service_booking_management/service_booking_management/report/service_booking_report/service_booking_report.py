# Copyright (c) 2025, Alfastack and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": "Booking ID",
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Service Booking",
			"width": 180
		},
		{
			"label": "Customer Name",
			"fieldname": "customer_name",
			"fieldtype": "Link",
			"options": "Customer",
			"width": 180
		},
		{
			"label": "Service Type",
			"fieldname": "service_type",
			"fieldtype": "Select",
			"width": 120
		},
		{
			"label": "Preferred Date/Time",
			"fieldname": "preferred_datetime",
			"fieldtype": "Datetime",
			"width": 180
		},
		{
			"label": "Status",
			"fieldname": "status",
			"fieldtype": "Select",
			"width": 120
		},
		{
			"label": "Created On",
			"fieldname": "creation",
			"fieldtype": "Datetime",
			"width": 180
		},
		{
			"label": "Modified On",
			"fieldname": "modified",
			"fieldtype": "Datetime",
			"width": 180
		}
	]

def get_data(filters):
	conditions = []
	
	if filters.get("service_type"):
		conditions.append(f"service_type = '{filters.get('service_type')}'")
	
	if filters.get("status"):
		conditions.append(f"status = '{filters.get('status')}'")
	
	where_clause = " AND ".join(conditions) if conditions else "1=1"
	
	data = frappe.db.sql(f"""
		SELECT 
			name,
			customer_name,
			service_type,
			preferred_datetime,
			status,
			creation,
			modified
		FROM 
			`tabService Booking`
		WHERE 
			{where_clause}
		ORDER BY 
			creation DESC
	""", as_dict=1)
	
	
	return data
