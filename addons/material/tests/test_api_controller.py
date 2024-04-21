from odoo.tests import HttpCase, tagged

@tagged('post_install', '-at_install')
class TestApiController(HttpCase):
    def test_create_material(self):
        # Create a new material via the API
        response = self.url_open('/api/material', data={'material_code': 'ABC123', 'material_name': 'Test Material', 'material_buy_price': 50})
        self.assertEqual(response.status_code, 200)
        material_id = response.json().get('id')
        self.assertTrue(material_id, "Material not created successfully")

        # Read the created material and verify its attributes
        response = self.url_open(f'/api/material/{material_id}')
        self.assertEqual(response.status_code, 200)
        material_data = response.json()
        self.assertEqual(material_data.get('material_code'), 'ABC123')
        self.assertEqual(material_data.get('material_name'), 'Test Material')
        self.assertEqual(material_data.get('material_buy_price'), 50)

    def test_read_all_materials(self):
        # Fetch all materials
        response = self.url_open('/api/material')
        self.assertEqual(response.status_code, 200)
        materials = response.json()
        self.assertIsInstance(materials, list)

