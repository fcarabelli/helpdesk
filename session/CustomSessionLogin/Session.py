import redis
import base64
from django.core import serializers
from datetime import timedelta
from django.conf import settings


def create_session(user):
    r = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
    )
    user_json = serializers.serialize('json', [user])
    base64_email = base64.b64encode(bytes(user.email, 'utf-8'))
    r.setex(base64_email, timedelta(minutes=settings.SESSION_TIME_MINUTES), value=user_json)
    return base64_email


def destroy_session(base64_email):
    r = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
    )
    r.delete(str(base64_email))


def user_authenticated(email):
    r = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
    )
    user = r.get(email)
    for obj in serializers.deserialize("json", user):
        usr = obj
    if usr is not None:
        return True
    else:
        return False