// Copyright (c) 2023, Athletic Classic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Catalog Share', {
	// refresh: function(frm) {

	// }
	setup: function (frm) {
		frm.set_query('customer_primary_contact', function (doc) {
			return {
				query: "erpnext.selling.doctype.customer.customer.get_customer_primary_contact",
				filters: {
					'customer': doc.customer
				}
			}
		})
	}

});
