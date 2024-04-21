from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.material'
    description = 'Material'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')],
                                    string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('material.supplier', string='Supplier Name', required=True)

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError("Material Buy Price must be more than 100.")
        