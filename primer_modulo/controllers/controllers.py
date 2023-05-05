# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleCreation(http.Controller):
#     @http.route('/module_creation/module_creation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_creation/module_creation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_creation.listing', {
#             'root': '/module_creation/module_creation',
#             'objects': http.request.env['module_creation.module_creation'].search([]),
#         })

#     @http.route('/module_creation/module_creation/objects/<model("module_creation.module_creation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_creation.object', {
#             'object': obj
#         })
