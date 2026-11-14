from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase


User = get_user_model()


class CustomUserIntegrationTests(TestCase):

    def test_user_is_saved_in_database(self):
        user = User.objects.create_user(
            email = "test@example.com",
            password = "TestPassword123!")

        saved_user = User.objects.get(pk = user.pk)
        #pk = id

        self.assertEqual(saved_user.email, "test@example.com")
        self.assertEqual(saved_user.status, User.Status.PENDING)

        self.assertTrue( 
            saved_user.check_password("TestPassword123!"))


    def test_email_must_be_unique(self):
        User.objects.create_user(
            email = "test@example.com",
            password = "TestPassword123!")

        with self.assertRaises(IntegrityError):
             with transaction.atomic():
                  User.objects.create_user(
                       email = "test@example.com",
                       password = "AnotherPassword123!",)


    def test_authentication_by_email(self):
        user = User.objects.create_user(
            email = "test@example.com",
            password = "TestPassword123!",)

        authenticated_user = authenticate(
            email = "test@example.com",
            password = "TestPassword123!",)

        self.assertEqual(authenticated_user, user)
