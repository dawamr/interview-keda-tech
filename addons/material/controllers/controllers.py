from odoo import http
from odoo.http import request
import json
from datetime import datetime

class ApiController(http.Controller):

    @http.route('/api/material', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **post):
        material = request.env['material.material'].sudo().create(post)
        return json.dumps(material.read())

    @http.route('/api/material/<int:id>', auth='public', methods=['GET'], csrf=False)
    def read_material(self, id):
        material = request.env['material.material'].sudo().browse(id)
        return json.dumps(material.read())

    @http.route('/api/material/<int:id>', auth='public', methods=['PUT'], csrf=False)
    def update_material(self, id, **post):
        material = request.env['material.material'].sudo().browse(id)
        material.sudo().write(post)
        return json.dumps(material.read())

    @http.route('/api/material/<int:id>', auth='public', methods=['DELETE'], csrf=False)
    def delete_material(self, id):
        material = request.env['material.material'].sudo().browse(id)
        material.sudo().unlink()
        return json.dumps({"message": "Material deleted"})
    
    @http.route('/api/material', auth='public', methods=['GET'], csrf=False)
    def read_all_materials(self, material_code=None, material_name=None, min_price=None, max_price=None, supplier_name=None):
        domain = []
        if material_code:
            domain.append(('material_code', '=', material_code))
        if material_name:
            domain.append(('material_name', 'ilike', material_name))
        if min_price:
            domain.append(('material_buy_price', '>=', float(min_price)))
        if max_price:
            domain.append(('material_buy_price', '<=', float(max_price)))
        if supplier_name:
            domain.append(('supplier_id.name', 'ilike', supplier_name))

        materials = request.env['material.material'].sudo().search_read(domain)

        # Convert datetime fields to string format
        for material in materials:
            for field_name, field_value in material.items():
                if isinstance(field_value, datetime):
                    material[field_name] = str(field_value)

        return json.dumps(materials)
