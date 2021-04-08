import mysql.connector
import hashlib
from django.conf import settings
from session.models import User
from session.CustomSessionLogin.Session import create_session
from datetime import datetime

username = "usuario.prueba@frm.utn.edu.ar"
password = "prueba1234"

m = hashlib.md5()
m.update(password.encode('utf-8'))
hashed_pass = m.hexdigest()

db = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='utn_development', raise_on_warnings=True)
cursor = db.cursor()
query = "SELECT id, (goto), username, password2 FROM mailbox WHERE (goto) = %s AND password2 = %s"
cursor.execute(query, (username, hashed_pass,))
user = cursor.fetchone()
print(user)