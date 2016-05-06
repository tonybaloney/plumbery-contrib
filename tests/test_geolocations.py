#!/usr/bin/env python

"""
Tests for `geolocations` module.
"""

from collections import namedtuple
import logging
import unittest


from plumbery_contrib.geolocations import PlumberyGeolocations


class TestPlumberyGeolocations(unittest.TestCase):

    def test_cities(self):
        database = PlumberyGeolocations()
        city = database.get_city('EU6')
        self.assertEqual(city, 'Frankfurt')
        city = database.get_city('xYz')
        self.assertEqual(city, '*unknown*')
        city = database.get_city(None)
        self.assertEqual(city, '*unknown*')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
