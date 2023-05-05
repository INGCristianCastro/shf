from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    servers_ids = fields.Many2many('shf.server', string="Servers")
    shf_employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Responsible",
    )
