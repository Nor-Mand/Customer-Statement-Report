# -*- coding: utf-8 -*-
from odoo import models, fields

class CustomerStatementWizard(models.TransientModel):
    _name = "customer.statement.report.wizard"

    partner_id = fields.Many2one('res.partner', string="Customer")


    def write(self, vals):
        if 'partner_id' in vals and vals['partner_id']:
            partner = self.env['res.partner'].browser(vals['partner_id'])
            print('#########',partner)
            vals['comment'] = partner.name
        
        return super().write(vals)