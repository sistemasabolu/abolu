# -*- coding: utf-8 -*-
{
    'name': "Website shop abolu",
    'summary': "Abolu: Website shop dev",
    'description': """
Abolu: Website shop dev
=======================
Task#1946350:
specific content to Logged Users:
The customer wants to have specific content for Logged users.
They want to use their website as a B2B portal for their customers
For the general public: They want to show products on the "Shop" page with the images,
but not show product prices, also they don't want the general public to make any purchase.

    """,
    'author': "Odoo, Inc",
    'website': "https://www.odoo.com",
    'category': 'Custom Development',
    'depends': ['website_sale'],

    'data': [
        "views/template.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
