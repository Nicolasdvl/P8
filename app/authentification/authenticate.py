"""
Custom authentification backends.

Allows authentification by email instead of username.
"""
from django.contrib.auth import get_user_model


UserModel = (
    get_user_model()
)  # récupère l'objet User même s'il a été modifié ailleurs


class EmailAuth:
    """Email authentication."""

    def user_can_authenticate(self, user):
        """Reject users with is_active=False."""
        is_active = getattr(user, "is_active", None)
        return is_active or is_active is None

    def authenticate(self, request, email=None, password=None, **kwargs):
        """Use email to replace username for authentification."""
        if email is None:
            email = kwargs.get(UserModel.EMAIL_FIELD)
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(
                user
            ):
                return user

    def get_user(self, user_id):
        """Return user if existing."""
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
