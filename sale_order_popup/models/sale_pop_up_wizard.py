# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderPopUp(models.TransientModel):
    _name = 'sale.order.popup'
    _description = 'Actualizar estado pedido'

    invoice_number = fields.Char(string='Nª de Factura')

    def update_sale_order(self):
        ctx = self.env.context.copy()
        active_ids = ctx.get('active_ids', False)
        sale_order_obj = self.env['sale.order']
        for sale in sale_order_obj.browse(active_ids):
            sale.invoice_status = 'invoiced'
            sale.x_studio_prueba = self.invoice_number


