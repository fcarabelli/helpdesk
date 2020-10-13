from django.shortcuts import render, redirect

from helpdeskapp.forms import QuestionForm


def addQuestion(request):
    # Creamos un formulario vacío
    form = QuestionForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = QuestionForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "helpdeskapp/addQuestion.html", {'form': form})