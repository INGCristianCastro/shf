# -*- coding: utf-8 -*-
{
    'name': "SHF Ventas Extendido",

    'summary': """
        shf_sale_extended
    """,

    'description': """
        Sale module extension
    """,

    'author': "Reyes Hernando Santana Perez - inghernandosan@gmail.com",
    'website': "https://shf.com.co",

    'category': 'Operations',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],


    'application': False,
    'license': 'LGPL-3',
}
