"""
This module provides functionality related to Product,Contact Us,Employee,salary.

Author: Mamta Yadav
Date: 6-12-2024
"""
from django.apps import AppConfig

class MyappConfig(AppConfig):
    """
    Configuration class for the 'myApp' Django app.

    Attributes:
        default_auto_field (str): Default auto field for model primary keys.
        name (str): Name of the app ('myApp').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myApp'
