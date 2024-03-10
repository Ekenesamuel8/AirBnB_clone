import unittest
from datetime import datetime
from your_module import BaseModel  # Replace 'your_module' with the actual module name

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_save_method_updates_updated_at(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict())
        self.assertCountEqual(f created_at and updated_at are in ISO format
        obj_dict.keys(), expected_keys)

        # Check i    for key in ['created_at', 'updated_at']:
														                self.assertTrue(
																                datetime.strptime(obj_dict[key], "%Y-%m-%dT%H:%M:%S.%f"),
																		                msg=f"Failed for {key} key"
																				            )

																					            # Check if __class__ key is present
																						            self.assertEqual(obj_dict['__class__'], 'BaseModel')

																							    if __name__ == '__main__':
																							        unittest.main()

