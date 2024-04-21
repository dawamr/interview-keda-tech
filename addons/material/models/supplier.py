from odoo import models, fields, api, _ 

class Supplier(models.Model):
    _name = 'material.supplier'
    _description = 'Supplier'

    supplier_name = fields.Char(string='Supplier Name', required=True)
    material_ids = fields.One2many('material.material', 'supplier_id', string='Materials')

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, record.supplier_name))
        return res