from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist
from django.test import SimpleTestCase


User = get_user_model()


class CustomUserTests(SimpleTestCase):

    def test_email_is_username(self):
        self.assertEqual(User.USERNAME_FIELD, "email")
        # email == email

        with self.assertRaises(FieldDoesNotExist):
            User._meta.get_field("username")
            #_meta — внутренний интерфейс Django для получения метаданных модели.  Метаданные включают названия полей, типы полей и другую информацию о модели.

        
    def test_default_status_is_pending(self):
        user = User(email = "test@example.com")

        self.assertEqual(user.status, User.Status.PENDING,)
        #user - object. User - это класс модели CustomUser.

    
    def test_create_user(self):
        with patch.object(User, "save", autospec = True) as save_mock:
            user = User.objects.create_user(
                email = "TEST@EXAMPLE.COM",
                password = "TESTPASSWOrD123!"
            )
        
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.status, User.Status.PENDING)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        save_mock.assert_called_once()


    def test_password_is_hashed(self):
        with patch.object(User, "save", autospec = True):
            user = User.objects.create_user(
                email = "test@example.com",
                password = "TestPassword123!"
            )

            self.assertNotEqual(user.password, "TestPassword123"    )

            self.assertTrue(user.check_password("TestPassword123!"))
            
            self.assertFalse(user.check_password("WrongPassword"))


    def test_create_superuser(self):
        with patch.object(User, "save", autospec = True):
            user = User.objects.create_superuser(
                email = "admin@example.com",
                password = "AdminPassword123!",)

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.status, User.Status.ACTIVE)


    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email = "",
                password="TestPassword123!",)    

    
    def test_superuser_cannot_have_invalid_flags(self):
        invalid_options = [
            {"is_staff": False},
            {"is_superuser": False},
            {"status": User.Status.PENDING}]
            # создание списка из трех словарей. Каждый словарь это отдельный сценарий, который мы хотим проверить.

        for options in invalid_options:
                # возьми каждый словарь из inv.._opt.. и положи его внутрь options

            with self.subTest(options = options):
                    # помощь определения какой именно сценарий пошел не прошел тестированаие 
                with self.assertRaises(ValueError):
                        # "Я ожидаю, что код внутри вызовет исключение ValueError. произойдет - успех"
                    User.objects.create_superuser(
                        email = "admin@example.com",
                        password = "AdminPassword123!",
                        **options,
                            # Оператор ** распаковывает словарь в именованные аргументы функции.
                    )

