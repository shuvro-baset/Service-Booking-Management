# Service Booking Management Module

## Project Description

This is a custom ERPNext module for managing service bookings in a wellness center.  
It includes a custom DocType, workflow state management, email notifications, custom reports, and print formats.

## Installation

1. Install Frappe/ERPNext (version 15)
2. Clone this repository into your bench apps folder by following command:  
   `bench get-app https://github.com/shuvro-baset/Service-Booking-Management`
3. Install the app in your site:  
   `bench --site yoursite install-app service_booking_management`
4. Run migrations:  
   `bench --site yoursite migrate`
5. Start the bench:  
   `bench start`

## Usage

- After successfull setup and migration you will get the custom doctype, reports, print formats, workflow, role and webhooks
- Create a new Service Booking from the Desk.
- Change status using the workflow actions (Requested → Approved → Completed).
- Email notifications are sent automatically on approval.
- Generate reports from the Reports module.
- Print booking confirmation using the custom print format.

## System Information

- OS: macOS Sequoia
- Python: 3.13.3
- frappe 15.67.0
- erpnext 15.60.1
- Editor: VS Code

## Features

- Custom DocType: Service Booking
- Workflow with automated status updates
- Email notifications on workflow state changes
- Custom report with filters
- Print format for booking confirmation
- (Optional) Webhook integration for external API

## Testing

- Create bookings and submit to trigger workflow.
- Check email inbox for notifications.
- Verify webhook calls in your external service.

## Video Demonstration

<iframe src="https://drive.google.com/file/d/126b7mT8MYJk_s4S2PQ81GWzcBz-CYZ1c/view?usp=sharing" width="640" height="480" allow="autoplay"></iframe>

## Contact

For any questions, please contact: md.abdul.baset75@gmail.com
