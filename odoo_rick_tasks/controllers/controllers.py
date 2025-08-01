# -*- coding: utf-8 -*-
# from odoo import http


# class OdooRickTasks(http.Controller):
#     @http.route('/odoo_rick_tasks/odoo_rick_tasks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_rick_tasks/odoo_rick_tasks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_rick_tasks.listing', {
#             'root': '/odoo_rick_tasks/odoo_rick_tasks',
#             'objects': http.request.env['odoo_rick_tasks.odoo_rick_tasks'].search([]),
#         })

#     @http.route('/odoo_rick_tasks/odoo_rick_tasks/objects/<model("odoo_rick_tasks.odoo_rick_tasks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_rick_tasks.object', {
#             'object': obj
#         })

