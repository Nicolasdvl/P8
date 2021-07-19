from django.contrib.auth import get_user_model


UserModel = (
    get_user_model()
)  # récupère l'objet User même s'il a été modifié ailleurs


class EmailAuth:
    """Email authentication."""

    def authenticate(self, request, email=None, password=None, **kwargs):
        print("REACH authenticate ========")
        print(password)
        if email is None:
            email = kwargs.get(UserModel.EMAIL_FIELD)
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            print("REACH userrrr")
            print(self.user_can_authenticate(user))
            print(user.check_password(password))
            if user.check_password(password) and self.user_can_authenticate(
                user
            ):
                print("USER CAN AUTH")
                return user

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, "is_active", None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
