# -*- coding: utf-8 -*-
{
    'name': "SHF Helpdesk Mgmt",

    'summary': """
        shf_helpdesk_mgmt   
    """,

    'description': """
        module extension helpdesk
    """,

    'author': "Cristian Camilo Castro - cristiancastromora1@gmail.com",
    'website': "https://shf.com.co",

    'category': 'Operations',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'helpdesk_mgmt',
        'hr',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket.xml',
        'views/shf_server.xml'
    ],

    'application': False,
    'license': 'LGPL-3',
}
