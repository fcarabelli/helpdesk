import mysql.connector
import hashlib
from django.conf import settings
from django.contrib.auth.hashers import check_password
from ..models import User


class UTNAuth(object):
    """
    Authenticates against UTN.
    """

    def authenticate(self, request, username, password, **kwargs):
        try:
            usuario = User.objects.get(email=username)
            usuario_pass_valido = usuario.check_password(password)
            if usuario_pass_valido and usuario.is_active:
                print(usuario)
                return usuario
            else:
                return None
        except User.DoesNotExist:
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            hashed_pass = m.hexdigest()
            try:
                db = mysql.connector.connect(**settings.UTN_CONFIG)
                cursor = db.cursor()
                query = "SELECT (goto), username, password2 FROM mailbox WHERE (goto) = %s AND password2 = %s"
                cursor.execute(query, (username, hashed_pass))
                user = cursor.fetchone()
                full_name = str.split(user[1])
                first_name = full_name[0]
                last_name = full_name[1]
                usr = User.objects.create_user(username=user[0], email=user[0], first_name=first_name, last_name=last_name, cellphone=0)
                usr.set_password(password)
                usr.save()
                return usr
            except mysql.connector.Error as err:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
