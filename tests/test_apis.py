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
    def setup_database_schema(self):
        ## connecting to the database using 'connect()' method
        ## it takes 3 required parameters 'host', 'user', 'passwd'
        db = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="root123"
        )

        ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
        cursor = db.cursor()
        #cursor.execute("CREATE DATABASE systeam_ecommerce")
        cursor.execute("SHOW DATABASES")

        ## 'fetchall()' method fetches all the rows from the last executed statement
        databases = cursor.fetchall()  ## it returns a list of all databases present

        ## printing the list of databases
        print(databases)



    """Test case for the client methods."""

    # Test of test_add_or_update_user API

    def setUp(self):
        self.setup_database_schema()

    def test_add_or_update_user(self):
        with app.test_client() as c:
            res = c.post('/user', json={"first_name": "Seller3", "last_name": "Seller3 lastname", "token": "Seller3token","email": "seller3@gmail.com"})

            # Passing the mock object
            response = {}
            data = json.loads(res.get_data(as_text=True))
            # Assert response
            self.assertEqual(data, response)

    def test_get_orders(self):
        with app.test_client() as c:
            res = c.get('/orders?email=seller3@gmail.com')

            # Passing the mock object
            response = []
            data = json.loads(res.get_data(as_text=True))
            # Assert response
            print(data)
            self.assertEqual(data, response)


if __name__ == '__main__':
    unittest.main()