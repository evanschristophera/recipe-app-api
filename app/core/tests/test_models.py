"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model # always able to get configured user model


class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Text creating a user with an email is successsful."""
        email = 'text@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


