# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.tools import ustr
from odoo.tools.pycompat import izip
from odoo import _, http

class WebsiteSale(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        if not ppg:
            ppg = 100 # customer requested default ppg to be 100
        if not post.get('order'):
            post['order'] = 'default_code asc'
            # post['order'] = 'display_name asc'
        return super(WebsiteSale, self).shop(page, category, search, ppg, **post)
        
    def _get_shop_payment_values(self, order, **kwargs):
        values = super(WebsiteSale, self)._get_shop_payment_values(order, **kwargs)
        if request.env.user._is_public():
            order.sudo().write({'is_from_new_customer': True})
            values['acquirers'] = [request.env.ref('abolu_website_sale.payment_acquirer_request_quotation')]
        return values
