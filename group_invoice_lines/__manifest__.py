# -*- coding: utf-8 -*-
{
    'name': "Group Invoice Lines",
    'summary': "Agrupa líneas de factura en el reporte PDF",
    'description': """
        Este módulo personaliza el reporte de facturas
        para agrupar líneas según ciertos criterios.
    """,
    'author': "Somme Sante TI",
    'website': "https://sommesante.com",
    'category': 'Accounting/Accounting',
    'version': '18.0.1.0.0',
    'depends': ['account_accountant', 'web_enterprise'],

    'data': [
        'views/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OEEL-1',
}
