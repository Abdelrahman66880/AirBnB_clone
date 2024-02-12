#!/usr/bin/python3
from models.base_model import BaseModel
import uuid
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    """Test case for the ModifiedModel class in the 'models' module."""

    def setUp(self):
        """Prepare the initial state for the tests."""
        self.instance_1 = BaseModel()
        self.instance_2 = BaseModel()

    
    def tearDown(self):
        """Clean up resources after each test."""
        del self.instance_1
        del self.instance_2

    def test_existanceInstance(self):
        """Checkin the existance of the class or not"""
        self.assertIsInstance(self.instance_1, BaseModel)

    def test_typeId(self):
        """Checking the type of the id"""
        self.assertIsInstance(self.instance_1, str)
    
    def test_uniqeId(self):
        """test the unique Id"""
        self.assertNotEqual(self.instance_1, self.instance_2)

    def test_to_dictMethod(self):
        """Testing the usage of the to_dict method"""
        dict_instance_1 = self.instance_1.to_dict()
        self.assertIsInstance(dict_instance_1, dict)

    def test_save_method(self):
        """Test the save() method of the ModifiedModel class.
        Assert that the 'updated_at' attribute before calling save() is not the same after calling save().
        """
        before_save = self.instance_1.updated_at
        after_save = self.instance_1.save()
        self.assertNotEqual(before_save, after_save)

    
if __name__ == "__main__":
    unittest.main()

