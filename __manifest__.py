# -*- coding: utf-8 -*-
{
    'name': "method_pos_order_line_resumen",

    'summary': """
        Este modulo amplia las funcionalidades del punto de venta
        agregar una opción en le menú para ver los totales por prodcutos. 
        Este modulo esta diseñado para puntos de venta restauran
        """,

    'description': """
        totaliza las cantidades por productos en las pantallas del restoran
    """,

    'author': "Method ERP",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','pos_restaurant',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}