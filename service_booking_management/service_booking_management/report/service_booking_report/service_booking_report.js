// Copyright (c) 2025, Alfastack and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking Report"] = {
	"filters": [
		{
			"fieldname": "service_type",
			"label": __("Service Type"),
			"fieldtype": "Select",
			"options": [
				"",
				"Therapy",
				"Spa",
				"Others"
			]
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": [
				"",
				"Requested",
				"Approved",
				"Completed"
			]
		}
	]
};
