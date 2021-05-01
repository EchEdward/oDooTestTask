# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductManufacturer(models.Model):
    _name = 'product_data.manufacturer'
    name = fields.Char(string='Manufacturer', required=True)


class ProductModel(models.Model):
    _name = 'product_data.model'

    name = fields.Char(string='Model', required=True)
    parent_field_id = fields.Many2one('product_data.manufacturer', string="Manufacturer")

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer = fields.Many2one('product_data.manufacturer', string="Manufacturer")
    model = fields.Many2one('product_data.model', string="Model")

    @api.onchange('manufacturer')
    def set_domain_for_model(self):
        model_obj = self.env['product_data.model'].search([('parent_field_id', '=', self.manufacturer.id)])
        models_list = [data.id for data in model_obj]
        self.model=False
        return {'domain': {'model': [('id','in',models_list)]}}