# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductController(BaseTestCase):
    """ProductController integration test stubs"""

    def test_add_product(self):
        """Test case for add_product

        Add a new product to the store
        """
        body = Product()
        response = self.client.open(
            '//product',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product(self):
        """Test case for delete_product

        Deletes a product
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '//product/{productId}'.format(productId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_by_id(self):
        """Test case for get_product_by_id

        Find product by ID
        """
        response = self.client.open(
            '//product/{productId}'.format(productId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Update an existing product
        """
        body = Product()
        response = self.client.open(
            '//product',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product_form(self):
        """Test case for update_product_form

        Updates a product in the store with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '//product/{productId}'.format(productId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
