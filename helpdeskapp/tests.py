from django.test import TestCase


from helpdeskapp.models import Question



class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(subject="Esto es una prueba",message="Esto es una prueba",urgency="HIGH")

    def test_question_recently_created(self):
        recent_creation = Question.objects.get(subject="Esto es una prueba")
        self.assertEqual(recent_creation.message, 'Esto es una prueba')
        self.assertEqual(recent_creation.urgency, 'HIGH')