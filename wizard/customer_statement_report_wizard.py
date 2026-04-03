# -*- coding: utf-8 -*-
from odoo import models, fields
from datetime import datetime

class CustomerStatementWizard(models.TransientModel):
    _name = "customer.statement.report.wizard"

    partner_id = fields.Many2one('res.partner', string="Customer")

    
    def action_print_report(self):
        self.ensure_one()
        # Get active partner
        partner = self.env['res.partner'].browse(self.env.context.get('active_id'))
        current_date = datetime.today().strftime("%d-%m-%Y")
        filename = f"{partner.name}_{current_date}"
        if partner:
            # testing get record in comments
            partner.comment = filename
        return {'type': 'ir.actions.act_window_close'}