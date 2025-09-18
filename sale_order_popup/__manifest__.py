# -*- coding: utf-8 -*-
{
    'name': "Sale Order Popup Wizard",
    'summary': "Wizard para actualizar pedidos de venta con número de factura",
    'description': """
        Este módulo agrega un asistente (popup) en los pedidos de venta
        que permite actualizar el estado y registrar el número de factura.
    """,
    'author': "Somme Sante TI",
    'website': "https://sommesante.com",
    'category': 'Sales/Sales',
    'version': '18.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_pop_up_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'OEEL-1',
}
