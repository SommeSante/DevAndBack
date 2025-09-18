# -*- coding: utf-8 -*-
{
    'name': "Group Invoice Lines",
    'summary': "Agrupa líneas de factura en el reporte PDF",
    'description': """
        Este módulo personaliza el reporte de facturas
        para agrupar líneas según ciertos criterios.
    """,
    'author': "Tu Empresa",
    'website': "https://www.tuempresa.com",
    'category': 'Accounting/Accounting',
    'version': '18.0.1.0.0',
    'depends': ['account'],   # no necesitas 'base', viene implícito
    'data': [
        'views/report_invoice.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
