# -*- coding: utf-8 -*-
from odoo import http

# class MethodPosOrderLineResumen(http.Controller):
#     @http.route('/method_pos_order_line_resumen/method_pos_order_line_resumen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_pos_order_line_resumen/method_pos_order_line_resumen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_pos_order_line_resumen.listing', {
#             'root': '/method_pos_order_line_resumen/method_pos_order_line_resumen',
#             'objects': http.request.env['method_pos_order_line_resumen.method_pos_order_line_resumen'].search([]),
#         })

#     @http.route('/method_pos_order_line_resumen/method_pos_order_line_resumen/objects/<model("method_pos_order_line_resumen.method_pos_order_line_resumen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_pos_order_line_resumen.object', {
#             'object': obj
#         })