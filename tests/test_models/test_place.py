#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlaceAttributes(unittest.TestCase):
    """
    Test case class for the Place attributes in the models.Place module.
    """

    def test_renamed_city_id(self):
        """
        Test if the renamed_city_id attribute of Place is a string and has the default
        value of an empty string.
        """
        self.assertIsInstance(Place.renamed_city_id, str)
        self.assertEqual(Place.renamed_city_id, "")

    def test_renamed_user_id(self):
        """ Test if the renamed_user_id attribute of Place is a string and has
        the default value of an empty string.
        """
        self.assertIsInstance(Place.renamed_user_id, str)
        self.assertEqual(Place.renamed_user_id, "")

    def test_renamed_name(self):
        """ Test if the "renamed_name" attribute of Place is a string and has the default
        value of an empty string.
        """
        self.assertIsInstance(Place.renamed_name, str)
        self.assertEqual(Place.renamed_name, "")

    def test_renamed_description(self):
        """ Test if the renamed_description attribute of Place is a string and
        has the default value of an empty string.
        """
        self.assertIsInstance(Place.renamed_description, str)
        self.assertEqual(Place.renamed_description, "")

    def test_renamed_number_rooms(self):
        """ Test if the renamed_number_rooms attribute of Place is an integer and
        has the default value of 0.
        """
        self.assertIsInstance(Place.renamed_number_rooms, int)
        self.assertEqual(Place.renamed_number_rooms, 0)

    def test_renamed_number_bathrooms(self):
        """ Test if the renamed_number_bathrooms attribute of Place is an integer
        and has the default value of 0.
        """
        self.assertIsInstance(Place.renamed_number_bathrooms, int)
        self.assertEqual(Place.renamed_number_bathrooms, 0)

    def test_renamed_max_guest(self):
        """ Test if the renamed_max_guest attribute of Place is an integer and has the
        default value of 0.
        """
        self.assertIsInstance(Place.renamed_max_guest, int)
        self.assertEqual(Place.renamed_max_guest, 0)

    def test_renamed_price_by_night(self):
        """ Test if the 'renamed_price_by_night' attribute of Place is an integer and
        has the default value of 0.
        """
        self.assertIsInstance(Place.renamed_price_by_night, int)
        self.assertEqual(Place.renamed_price_by_night, 0)

    def test_renamed_latitude(self):
        """ Test if the renamed_latitude attribute of Place is a float and has the
        default value of 0.0.
        """
        self.assertIsInstance(Place.renamed_latitude, float)
        self.assertEqual(Place.renamed_latitude, 0.0)

    def test_renamed_longitude(self):
        """ Test if the 'renamed_longitude' attribute of Place is a float and has the
        default value of 0.0.
        """
        self.assertIsInstance(Place.renamed_longitude, float)
        self.assertEqual(Place.renamed_longitude, 0.0)

if __name__ == '__main__':
    unittest.main()

