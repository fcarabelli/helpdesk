import mysql.connector
import hashlib
from django.conf import settings
from django.utils.crypto import get_random_string
from ..models import User


class UTNAuth(object):
    """
    Authenticates against UTN.
    """

    def authenticate(self, request, username, password, **kwargs):
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        hashed_pass = m.hexdigest()
        try:
            db = mysql.connector.connect(**settings.UTN_CONFIG)
            cursor = db.cursor()
            query = "SELECT (goto), username, password2 FROM mailbox WHERE (goto) = %s AND password2 = %s"
            cursor.execute(query, (username, hashed_pass))
            user = cursor.fetchone()
            if user is not None:
                try:
                    usuario = User.objects.get(email=user[0])
                    return usuario
                except User.DoesNotExist:
                    full_name = str.split(user[1])
                    first_name = full_name[0]
                    last_name = full_name[1]
                    usr = User.objects.create_user(username=user[0], email=user[0], first_name=first_name,
                                                   last_name=last_name, cellphone=0)
                    usr.set_password(get_random_string().upper())
                    usr.save()
                    return usr
            else:
                return None
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
