from django.test import TestCase
from session.models import User
from session.forms import LoginForm


class SessionTestCase(TestCase):

    def test_verificarqueseusecorreoinstitucional(self):
        form = LoginForm(data={'user_email': 'fedegallar2006@hotmail.com', 'password': '123456789'})
        self.assertFalse(form.is_valid())

    def test_verificarqueseusecorreodocente(self):
        form = LoginForm(data={'user_email': 'federico.gallardo@docentes.frm.utn.edu.ar', 'password': '123456789'})
        self.assertTrue(form.is_valid())

    def test_verificarqueseusecorreonodocente(self):
        form = LoginForm(data={'user_email': 'federico.gallardo@frm.utn.edu.ar', 'password': '123456789'})
        self.assertTrue(form.is_valid())

    def test_verificarqueseusecorreoalumno(self):
        form = LoginForm(data={'user_email': 'federico.gallardo@alumnos.frm.utn.edu.ar', 'password': '123456789'})
        self.assertTrue(form.is_valid())
