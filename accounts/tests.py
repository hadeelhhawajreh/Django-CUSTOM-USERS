from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import CustomUser

# Create your tests here.

class CRUDTests(TestCase):
    def test_login_status(self):
        response = self.client.get(reverse('accounts/login/'))
        self.assertEqual(reverse('accounts/login/').status_code, 302)
    def test_login_status(self):
        response = self.client.get(reverse('accounts/logout/'))
        self.assertEqual(response.status_code, 302)

  

    