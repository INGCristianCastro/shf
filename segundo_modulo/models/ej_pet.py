# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age', required=True)
    color = fields.Char(string='color', required=True)
    is_new = fields.Boolean(string='is_new', default=True)
    type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('other', 'Others')], string='type', default="dog", required=True)
