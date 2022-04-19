import string

from django.utils.crypto import get_random_string
from .models import Person

from celery import shared_task

@shared_task
def get_data(data):
    name = data['name']
    for i in range(len(name)):
        name = f"{name}{get_random_string(length=2, allowed_chars=string.ascii_letters)}"
        Person.objects.create(name=name)
    return f"{len(name)} random persons were created"