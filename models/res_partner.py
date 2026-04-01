# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import datetime

class ResPartnerReportStatement(models.Model):
    _inherit = "res.partner"

    # Function to export the filename in PDF with the customer name and current date
    def _get_filename_PDF(self):
        current_date = datetime.today().strftime('%d-%m-%Y')
        customer_name = self.name
        filename = f"Statement_report({customer_name}_{current_date})"
        print(filename)