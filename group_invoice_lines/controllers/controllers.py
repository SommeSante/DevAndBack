# -*- coding: utf-8 -*-
# from odoo import http


# class GroupInvoiceLines(http.Controller):
#     @http.route('/group_invoice_lines/group_invoice_lines/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/group_invoice_lines/group_invoice_lines/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('group_invoice_lines.listing', {
#             'root': '/group_invoice_lines/group_invoice_lines',
#             'objects': http.request.env['group_invoice_lines.group_invoice_lines'].search([]),
#         })

#     @http.route('/group_invoice_lines/group_invoice_lines/objects/<model("group_invoice_lines.group_invoice_lines"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('group_invoice_lines.object', {
#             'object': obj
#         })
