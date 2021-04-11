from celery import shared_task
from helpdeskapp.models import Question
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from time import sleep

@shared_task
def send_async_html_message(question_id):
    question = Question.objects.get(pk=question_id)
    body = question.message
    subject = question.subject
    mail_to = question.email
    question_datetime = str(question.question_datetime)
    mail_body = render_to_string('helpdeskapp/mail.html', {'subject': subject, 'body': body, 'mail_to': mail_to,
                                                           'request_datetime': question_datetime,
                                                           'question_number': question_id})
    msg = EmailMessage('NO RESPONDER - Consulta N°: ' + str(question_id) + ' - ' + subject, mail_body,
                       'Sistema de Mesa de Ayuda FRM UTN', [mail_to])
    msg.content_subtype = "html"
    return msg.send()
