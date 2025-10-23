# -*- coding: utf-8 -*-
{
    'name': "Empleados por Planta",
    'summary': "Gestión de empleados asignados a distintas plantas",
    'description': """
        Este módulo permite administrar y relacionar empleados
        con las plantas de la empresa, agregando vistas y accesos
        personalizados sobre pedidos de venta.
    """,
    'author': "Somme Sante TI",
    'website': "https://sommesante.com",
    'category': 'Human Resources',
    'version': '18.0.1.0.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_pop_up_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
