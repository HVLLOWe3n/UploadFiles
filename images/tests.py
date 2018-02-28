from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from .models import SimpleModel


class SimpleTest(TestCase):
    def setUp(self):
        self.c = Client

    def test_simple_model(self):
        pass
