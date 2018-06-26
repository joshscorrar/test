import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def add_product(body):  # noqa: E501
    """Add a new product to the store

     # noqa: E501

    :param body: product object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_product(productId, api_key=None):  # noqa: E501
    """Deletes a product

     # noqa: E501

    :param productId: Product id to delete
    :type productId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_product_by_id(productId):  # noqa: E501
    """Find product by ID

    Returns a single product # noqa: E501

    :param productId: ID of product to return
    :type productId: int

    :rtype: Product
    """
    return 'do some magic!'


def update_product(body):  # noqa: E501
    """Update an existing product

     # noqa: E501

    :param body: Product object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_product_form(productId, name=None, status=None):  # noqa: E501
    """Updates a product in the store with form data

     # noqa: E501

    :param productId: ID of product that needs to be updated
    :type productId: int
    :param name: Updated name of the product
    :type name: str
    :param status: Updated status of the product
    :type status: str

    :rtype: None
    """
    return 'do some magic!'
