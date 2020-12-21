from datetime import datetime, timedelta
from django.conf import settings
from .CustomSessionLogin.Session import destroy_session

class AutoLogout:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'current_user_session' not in request.session:
            response = self.get_response(request)
            return response
        if datetime.now() - request.session['login_time_user_session'] > timedelta(0,
                                                                                   settings.SESSION_TIME_MINUTES * 60,
                                                                                   0):
            del request.session['login_time_user_session']
            del request.session['current_user']
        else:
            request.session['current_user_session'] = datetime.now()
        response = self.get_response(request)
        return response
