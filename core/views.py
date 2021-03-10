from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from helpdeskapp.models import Question
from helpdesk import settings
import mysql.connector
import hashlib


# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = User.objects.filter(username=request.session['user'])[0]
        user_questions =  Question.objects.filter(email=request.session['user'])
        request_session = request.session
        param = {'current_user': current_user,
                 'request_session': [i for i in request_session.items()],
                 'user_questions': user_questions
                 }
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')


''' 
    This function performs the validation of user credentials
    communicating with the external system
 '''
def authenticate(username=None, password=None, **kwargs):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    hashed_pass = m.hexdigest()
    try:
        db = mysql.connector.connect(**settings.UTN_CONFIG)
        cursor = db.cursor()
        query = "SELECT id, (goto), username, phone FROM mailbox WHERE (goto) = %s AND password2 = %s"
        cursor.execute(query, (username, hashed_pass,))
        user = cursor.fetchone()
        usr = User(username=user[1], first_name=user[1].split('.')[0].capitalize(), last_name=user[1].split('.')[1].split('@')[0].capitalize(), phone_number=user[3])
        usr.pk = user[0]
        cursor.close()
        db.close()
        return usr
    except mysql.connector.Error as err:
        return None




def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        #check_user = User.objects.filter(username=uname, password=pwd)
        try:
            check_user = authenticate(request=request, username=uname, password=pwd )
            check_user.save()
            request.session['user'] = uname
            return redirect('home')
        except:
            return HttpResponse('Please enter valid Username or Password.')
    return render(request, 'login.html')


def logout(request):
    try:
        uname = request.session['user']
        check_user = User.objects.filter(username=uname)
        if check_user:
            check_user[0].delete()
            del request.session['user']
    except:
        return redirect('login')
    return redirect('login')