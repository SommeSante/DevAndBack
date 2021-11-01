# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    def group_lines(self):
        lines = []
        invoice_lines = self.invoice_line_ids.sorted(key=lambda l: (-l.sequence, l.date, l.move_name, -l.id), reverse=True)
        lines_dict = {}
        for line in invoice_lines:
            if line.product_id.id not in lines_dict:
                lines_dict[line.product_id.id] = [
                    line.display_type,
                    line.name,
                    line.quantity,
                    line.product_uom_id.name,
                    line.price_unit,
                    line.product_uom_id.unspsc_code_id.code if line.product_uom_id.unspsc_code_id else '',
                    line.discount,
                    line.tax_ids,
                    line.price_subtotal,
                    line.price_total,
                    line.product_id.unspsc_code_id.code if line.product_id.unspsc_code_id else '',

                ]
            elif not line.product_id and line.display_type == 'line_section':
                lines_dict[line.name] = [
                    line.display_type,
                    line.name
                ]
            else:
                lines_dict[line.product_id.id][2] += line.quantity
                # lines_dict[line.product_id.id][4] += line.quantity
                lines_dict[line.product_id.id][8] += line.price_subtotal
                lines_dict[line.product_id.id][9] += line.price_total
        for value in lines_dict:
            lines.append(lines_dict[value])

        return lines

