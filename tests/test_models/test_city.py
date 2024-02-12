import unittest
from models.City import City
from models.base_model import BaseModel


class TestRenamedCityClass(unittest.TestCase):
    """
    Test case class for the RenamedCity class in the models.city module.
    """
    def test_instance_creation(self):
        """ 
        Test if RenamedCity object is successfully created.
        """
        renamed_city_instance = City()
        self.assertIsInstance(renamed_city_instance, City)

    def test_inheritance(self):
        """ 
        Test if RenamedCity class inherits from RenamedBaseModel.
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_state_id_attribute(self):
        """ 
        Test if state_id attribute is present in the RenamedCity class.
        """
        self.assertTrue(hasattr(City, 'state_id'))

    def test_state_id_attribute_type(self):
        """ 
        Test if 'state_id' attribute in RenamedCity is a string.
        """
        self.assertIsInstance(City.state_id, str)

    def test_renamed_attribute(self):
        """ 
        Test if 'renamed_attribute' attribute is present in the RenamedCity class.
        """
        self.assertTrue(hasattr(City, 'renamed_attribute'))

    def test_renamed_attribute_type(self):
        """ 
        Test if 'renamed_attribute' attribute in RenamedCity is a string.
        """
        self.assertIsInstance(City.renamed_attribute, str)


if __name__ == '__main__':
    unittest.main()

