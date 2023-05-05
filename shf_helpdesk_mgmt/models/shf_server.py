# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShfServer(models.Model):
    _name = 'shf.server'
    _description = 'Shf Server'

    name = fields.Char(string="Name of server")

