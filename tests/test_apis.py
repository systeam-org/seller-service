"""Tests for Basic Functions"""
import sys
import json
import unittest
import mysql.connector
sys.path.append("../..")
from app import *

## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

class TestFunctions(unittest.TestCase):

    """Test case for the client methods."""

    # Test of get_orders API
    def test_get_orders(self):
        with app.test_client() as c:
            res = c.get('/orders?email=seller@gmail.com')

            # Passing the mock object
            response = [{'order_id': 1, 'total_amount': 14, 'created_on': '2019-11-24 18:59:38', 'status': 'Ordered', 'products': [{'product_name': 'T-Shirt', 'product_id': 1,'quantity': 2, 'unit_cost': 7}]}, {'order_id': 2, 'total_amount': 7, 'created_on': '2019-11-24 23:14:45', 'status': 'Ordered', 'products': [{'product_name': 'T-Shirt', 'product_id': 1, 'quantity': 1, 'unit_cost': 7}]}]
            data = json.loads(res.get_data(as_text=True))
            # Assert response
            print(data)
            self.assertEqual(data, response)


if __name__ == '__main__':
    unittest.main()