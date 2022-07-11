#!/usr/bin/python3
"""Defines a class BaseModelTest"""


import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """Defines tests for Base class"""
    
    def setUp(self):
        """ Method invoked for each test """
        self.new_base = Base(id=1)
        
    # def tearDown(self):
    #     Base.query.delete()

    # def test_check_instance_variables(self):
    #     self.assertEquals(self.new_base.id, 'django')
