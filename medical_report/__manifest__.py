# -*- coding: utf-8 -*-
{
    'name': "Medical Report",
    'summary': "Gestión y generación de reportes médicos",
    'description': """
        Este módulo permite generar, gestionar y personalizar reportes médicos.
        Incluye vistas XML para informes y puede expandirse con QWeb templates.
    """,
    'author': "Somme Sante TI",
    'website': "https://sommesante.com",
    'category': 'Human Resources',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        'views/examen_medico_report.xml',
        # 'views/report.xml',   # Descomenta si quieres cargar este archivo
    ],
    'qweb': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
