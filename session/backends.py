from django.contrib.auth.backends import ModelBackend
from session.models import User


class UserEmailModelBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
