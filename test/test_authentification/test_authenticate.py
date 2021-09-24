from django.test import TestCase
from authentification.models import User
from authentification.authenticate import EmailAuth


class TestAutheticate(TestCase):

    fixtures = ["test_users.json"]

    def test_user_can_authenticate(self):
        user = User.objects.get(id=1)
        self.assertTrue(EmailAuth.user_can_authenticate(EmailAuth, user))

    def test_get_user(self):
        auth_engine = EmailAuth()
        self.assertEqual(auth_engine.get_user(1), User.objects.get(id=1))
        self.assertEqual(auth_engine.get_user(5), None)

    def test_authenticate(self):
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
