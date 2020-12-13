from datetime import datetime


from django.shortcuts import render, redirect


from helpdesk.settings import EMAIL_HOST_USER
from helpdeskapp.forms import QuestionForm, AuthQuestionForm
from django.core.mail import send_mail, EmailMessage


def addQuestion(request):
    # We create an empty form
    if request.user.is_anonymous:
        form = QuestionForm()
    else:
        form = AuthQuestionForm()
    # We check if the form has been sent
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
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
            print(send_html_message(request))
            # After saving we redirect to the list
            return redirect('/')

    # If we reach the end we render the form
    return render(request, "helpdeskapp/addQuestion.html", {'form': form})


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

def send_html_message(request):
    if request.user.is_anonymous:
        mail_to = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['message']
    else:
        mail_to = request.user.email
        subject = request.POST['subject']
        body = request.POST['message']
    body = f'<body><h1>Sistema de mesa de ayuda FRM UTN</h1><br><h2>Su consulta está siendo procesada</h2><h3> Datos de la solicitud</h3><br><p>Solicitante: {mail_to}</p><br><p>{subject}</p><br><p>Consulta realizada: {body}</p><br><p>Fecha y Hora de la solicitud:{datetime.now().isoformat()}</p></body>'
    msg = EmailMessage(subject, body, EMAIL_HOST_USER, [mail_to])
    msg.content_subtype = "html"
    return msg.send()