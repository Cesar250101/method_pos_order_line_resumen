# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    categ_id = fields.Many2one(string='Categoría del Producto',related="product_id.product_tmpl_id.pos_categ_id")
    
    
    
