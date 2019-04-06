# -*- coding: utf-8 -*-
{
    'name': 'Abolu: Website Quotation',
    'summary': 'Abolu: Website Quotation',
    'description':
    """
Task ID: 1958553
Abolu needs to add the following functionality to their Website:
1. Feature 1:Public Users should be able to select products, like in an "Add to Cart" and request a Quotation for the products selected. 
- A Request Quotation button should be added to the page  https://abolu.odoo.com/shop/product/ with the same functionality as the Add to cart. This should be visible for both public and registered users
-after selecting the products and the quantities the public users or registered users should be able to specify their email address and select the option "Send Quotation by email"
- Once the quotation is sent  by email it should also be created in the backend
2) Feature 2
In the Shop page add the controls to define the number of products to show, by default it shows 20 products but Aboulu wants to allow the user to select 20,50,80 or 100 products to show.
    """,
    'license': 'OEEL-1',
    'author': 'Odoo Inc',
    'version': '0.1',
    'depends': ['website_sale', 'sale_management', 'website_dev_abolu'],
    'data': [
        'views/payment_acquirer_template.xml',
        'data/payment_acquirer_data.xml',
        'data/mail_template_data.xml',
        'views/templates.xml',
        'report/sale_order.xml',
    ],
}
