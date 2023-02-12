# -*- coding: utf-8 -*-

{
    'name': 'Supplier auto assignment of reference',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Inventory/Purchase',
    'summary': 'Supplier auto assignment of reference',
    'description': "",
    'depends': [
        'sale',
    ],
    'data': [
        'data/supplier_auto_ref_sequences.xml',
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
