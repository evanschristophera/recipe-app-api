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

    def test_new_user_mail_normalized(self):
        """test email is normalized for new users."""
        sample_emails=[
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)