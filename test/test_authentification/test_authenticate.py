from django.test import TestCase
from authentification.models import User
from authentification.authenticate import EmailAuth


class TestAutheticate(TestCase):
    """Test EmailAuth class."""

    fixtures = ["test_users.json"]

    def test_user_can_authenticate(self):
        """
        Test 'EmailAuth.user_can_authenticate()'.

        - First assert use a user with 'is_active=True' (default value) and
        should return 'True'.
        - Second assert use a user with 'is_active=False' and should return
        'None'.
        """
        user = User.objects.get(id=1)
        self.assertTrue(EmailAuth.user_can_authenticate(EmailAuth, user))

    def test_get_user(self):
        """
        Test 'EmailAuth.get_user()'.

        - Fisrt assert use an id existing in fixture and should return a user.
        - Second assert use an id not existing in fixture and shuld return
        'None'.
        """
        auth_engine = EmailAuth()
        self.assertEqual(auth_engine.get_user(1), User.objects.get(id=1))
        self.assertEqual(auth_engine.get_user(5), None)

    def test_authenticate(self):
        """
        Test 'EmailAuth.authenticate()'.

        - First assert use valid email and password and should return a user.
        - Second assert use unvalid email and should return 'None'.
        - Third assert use unvalid password and shoul return 'None'.
        """
        auth_engine = EmailAuth()
        request = None
        self.assertEqual(
            auth_engine.authenticate(request, "john@email.com", "mdp"),
            User.objects.get(id=1),
        )
        self.assertIsNone(
            auth_engine.authenticate(request, "notjohn@email.com", "mdp")
        )
        self.assertIsNone(
            auth_engine.authenticate(request, "john@email.com", "wrongmdp")
        )
