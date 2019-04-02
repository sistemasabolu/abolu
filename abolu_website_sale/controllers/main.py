# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.tools import ustr
from odoo.tools.pycompat import izip
from odoo import _

class WebsiteSale(WebsiteSale):

    def _get_shop_payment_values(self, order, **kwargs):
        values = super(WebsiteSale, self)._get_shop_payment_values(order, **kwargs)
        if not request.session.login or request.session.login == 'public':
            values['acquirers'] = [request.env.ref('abolu_website_sale.payment_acquirer_request_quotation')]
        return values
