# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class StockQuant(models.Model):
    _inherit = "stock.quant"

    categ_id = fields.Many2one('product.category',related='product_id.categ_id',readonly=True,store=True)