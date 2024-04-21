# -*- coding: utf-8 -*-
{
    'name': "material",

    'summary': """
        Module Material to handle material and suppliers""",

    'description': """
        Module Material to handle material and suppliers
    """,

    'author': "Dawam Raja",
    'website': "https://dawamraja.pro",
    'category': 'Beta',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'data/supplier_data.xml',
        'data/material_data.xml',
        'views/material.xml',
        'views/supplier.xml',

    ],
}
