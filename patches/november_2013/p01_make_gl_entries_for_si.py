# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

import webnotes

def execute():
	si_no_gle = webnotes.conn.sql("""select si.name from `tabSales Invoice` si 
		where docstatus=1 and not exists(select name from `tabGL Entry` 
			where voucher_type='Sales Invoice' and voucher_no=si.name)""")

	for si in si_no_gle:
		webnotes.get_obj("Sales Invoice", si[0]).make_gl_entries()