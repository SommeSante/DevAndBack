# -*- coding: utf-8 -*-
{
    'name': "Bitácora de Consultas",
    'summary': "Registro de consultas médicas o administrativas",
    'description': """
        Este módulo permite llevar un control y bitácora de las consultas,
        almacenando información relevante para seguimiento y reportes.
    """,
    'author': "Tu Empresa",
    'website': "https://www.tuempresa.com",
    'category': 'Extra Tools',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/bitacora_consulta_views.xml',
        # 'views/menus.xml',   # opcional si quieres menú propio
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
