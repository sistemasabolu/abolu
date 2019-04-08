# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_from_new_customer = fields.Boolean('Order from a New Customer')
    
    @api.multi
    def action_quotation_send(self):
        values = super(SaleOrder, self).action_quotation_send()
        if values.get('context'):
            try:
                template_id = self.env['ir.model.data'].get_object_reference('abolu_website_sale', 'email_template_edi_sale_abolu')[1]
            except ValueError:
                template_id = False
            values['context'].update({'default_template_id': template_id})
        return values
