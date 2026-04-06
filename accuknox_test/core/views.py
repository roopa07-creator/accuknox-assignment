from django.http import HttpResponse
from .models import TestModel
import threading

from django.db import transaction
from django.http import HttpResponse
from .models import TestModel

def test_signal(request):
    try:
        with transaction.atomic():
            TestModel.objects.create(name="Test")
    except:
        print("Transaction rolled back")

    return HttpResponse("Done")