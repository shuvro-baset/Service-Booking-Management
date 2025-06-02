# Copyright (c) 2025, Alfastack and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class ServiceBooking(Document):
	def on_submit(self):
		if self.status == 'Approved':
			customer_ref = frappe.get_doc('Customer', self.customer_name)
			if customer_ref.get('email_id'):
				message = f"""
								<p>Dear {self.customer_name},</p>
								<p>Your <strong>{self.service_type}</strong> session has been <strong>approved</strong>.</p>
								<p><strong>Preferred Date & Time:</strong> {frappe.format_value(self.preferred_datetime, self.meta.get_field("preferred_datetime"))}</p>
								<p>We look forward to welcoming you at our Wellness Center.</p>
								<br>
								<p>Best regards,<br>Wellness Center Team</p>
							"""

				frappe.sendmail(
					recipients=customer_ref.get('email_id'),
					subject="Your Booking is Approved",
					message=message
				)
			else:
				frappe.throw(_("The customer <b>{0}</b> has not set any email id yet. Please set a valid email id.").format(self.customer_name))