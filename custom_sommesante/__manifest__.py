# -*- coding: utf-8 -*-
{
    'name': "Custom Sommesante",
    'summary': "Personalizaciones para el proyecto Sommesanté",
    'description': """
        Módulo de personalización para Sommesanté.
        Incluye configuraciones de seguridad y ajustes específicos
        en modelos y vistas.
    """,
    'author': "Sommesanté IT",
    'website': "https://www.sommesante.com",
    'category': 'Extra Tools',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/service_medical_security.xml',
    ],
    'qweb': [],
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}
