from django.shortcuts import render, redirect
from django.forms import modelformset_factory

from helpdeskapp.forms import QuestionForm
from helpdeskapp.models import Question


def addQuestion(request):
    # We create an empty form
    # We check if the form has been sent
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        if request.user.is_anonymous:
            formset = modelformset_factory(Question, form=QuestionForm, fields=("subject", "message"))
        else:
            formset = modelformset_factory(Question, form=QuestionForm,fields=("email", "phone_number", "subject", "message"))

        if formset.is_valid():
            # We save the form but without confirming it,
            # so we will get an instance to handle it
            instancia = formset.save(commit=False)

            # We can save it whenever we want
            instancia.save()
            # After saving we redirect to the list
            return redirect('/')

    if request.user.is_anonymous:
        formset = modelformset_factory(Question, form=QuestionForm, fields=("subject", "message"))
    else:
        formset = modelformset_factory(Question, form=QuestionForm,fields=("email", "phone_number", "subject", "message"))

    # If we reach the end we render the form
    return render(request, "helpdeskapp/addQuestion.html", {'formset': formset})