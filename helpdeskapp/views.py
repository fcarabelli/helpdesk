from django.shortcuts import render, redirect

from helpdeskapp.forms import QuestionForm
from django.core.mail import send_mail

def addQuestion(request):
    # We create an empty form
    form = QuestionForm()

    # We check if the form has been sent
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = QuestionForm(request.POST)
        # If the form is valid ...
        if form.is_valid():
            # We save the form but without confirming it,
            # so we will get an instance to handle it
            instancia = form.save(commit=False)
            # We can save it whenever we want
            instancia.save()
            # After saving we redirect to the list
            send_mail('asunto', 'mensaje', 'fedegallar2006@hotmail.com', ['fedegallar2006@gmail.com'], fail_silently=False)
            return redirect('addQuestion')

    # If we reach the end we render the form
    return render(request, "helpdeskapp/addQuestion.html", {'form': form})