import mysql.connector
import hashlib
from django.conf import settings
from ..models import User
from .Session import create_session
from datetime import datetime

class UTNAuth:
    """
    Authenticates against UTN.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        hashed_pass = m.hexdigest()
        try:
            db = mysql.connector.connect(**settings.UTN_CONFIG)
            cursor = db.cursor()
            query = "SELECT goto, username, password2 FROM %s WHERE username=%s AND password2=%s;"
            cursor.execute(query, (settings.UTN_DB_TABLE, username, hashed_pass))
            user = cursor.fetchone()
            usr = User(email=user[0], first_name=user[1], last_name="", password=user[2], is_staff=True, is_active=True, date_joined=None, is_superuser=True, last_login=None, cellphone=None)
            usr.pk = user[0]
            encoded_email = create_session(usr)
            request.session['current_user_session'] = encoded_email
            request.session['current_user'] = usr
            request.session['login_time_user_session'] = datetime.now()
            request.session.modified = True
            cursor.close()
            db.close()
            return usr
        except mysql.connector.Error as err:
            return None

    def get_user(self, user_id):
        try:
            db = mysql.connector.connect(**settings.UTN_CONFIG)
            cursor = db.cursor()
            query = "SELECT goto, username, password2 FROM utn_development.mailbox WHERE id=%s;"
            cursor.execute(query, (str(user_id)))
            user = cursor.fetchone()
            usuario = User(
                           email=user[0],
                           first_name=user[1],
                           last_name="",
                           password=user[2],
                           is_staff=True,
                           is_active=True,
                           date_joined=None,
                           is_superuser=True,
                           last_login=None,
                           cellphone=None)
            usuario._meta.pk = user[0]
            cursor.close()
            db.close()
            return usuario
        except mysql.connector.Error as err:
            return None