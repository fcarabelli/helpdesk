
from django.shortcuts import render, redirect


from helpdesk.settings import EMAIL_HOST_USER
from helpdeskapp.forms import QuestionForm, AuthQuestionForm
from django.core.mail import send_mail, EmailMessage

from django_q.tasks import async_task
from time import sleep


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

            # creating asynchronous email sending

            async_task("helpdeskapp.tasks.send_async_html_message", instancia.id, timeout=120)

            # After saving we redirect to the list
            return redirect('/')

    # If we reach the end we render the form
    return render(request, "helpdeskapp/addQuestion.html", {'form': form})

