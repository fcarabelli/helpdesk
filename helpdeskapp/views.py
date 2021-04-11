from datetime import datetime

from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from helpdesk.settings import EMAIL_HOST_USER
from helpdeskapp.forms import QuestionForm, AuthQuestionForm
from django.core.mail import send_mail, EmailMessage

from helpdeskapp.tasks import send_async_html_message


def addQuestion(request):
    # We create an empty form
    if request.user.is_anonymous:
        form = QuestionForm()
    else:
        form = AuthQuestionForm()
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_active:
            form = AuthQuestionForm(data=request.POST)
        else:
            form = QuestionForm(data=request.POST)

        if form.is_valid():
            # We save the form but without confirming it,
            # so we will get an instance to handle it
            instancia = form.save(commit=False)

            if isinstance(form, AuthQuestionForm):
                instancia.email = request.user.email
                instancia.phone_number = request.user.cellphone or 0

            # We can save it whenever we want
            instancia.save()

            send_async_html_message.delay(instancia.id)
            # After saving we redirect to the list
            return redirect('/')

    # If we reach the end we render the form
    return render(request, "helpdeskapp/addQuestion.html", {'form': form})


def index(request):
    return render(request, "helpdeskapp/index.html")


def send_simple_message(request):
    if request.user.is_anonymous:
        mail_to = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['message']
    else:
        mail_to = request.user.email
        subject = request.POST['subject']
        body = request.POST['message']
    return send_mail(subject, body, EMAIL_HOST_USER, [mail_to])


def send_html_message(request, question_fields):
    if request.user.is_anonymous:
        mail_to = request.POST['email']
        subject = request.POST['subject']
    else:
        mail_to = request.user.email
        subject = request.POST['subject']
    body = request.POST['message']
    question_number = str(question_fields['number'])
    question_datetime = str(question_fields['datetime'])

    mail_body = render_to_string('helpdeskapp/mail.html', {'subject': subject, 'body': body, 'mail_to': mail_to,
                                                           'request_datetime': question_datetime,
                                                           'question_number': question_number})
    msg = EmailMessage('NO RESPONDER - Consulta N°: ' + question_number + ' - ' + subject, mail_body,
                       'Sistema de Mesa de Ayuda FRM UTN', [mail_to])
    msg.content_subtype = "html"
    return msg.send()
