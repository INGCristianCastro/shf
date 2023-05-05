
from odoo import models, fields, api


class ModuloRegistro(models.Model):
    _name = 'modulo_registro'
    _description = 'Modulo Registro'

    name = fields.Char(
        string='Name',
        required=True,
    )
