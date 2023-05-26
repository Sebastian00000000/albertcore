from typing import Any
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from django.http import HttpRequest, HttpResponse
from django.core.serializers import serialize
from .models import *

# Create your views here.


class TapeView(ListView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        tapes = Tape.objects.all()
        return render(request, 'tapes.html', {
            'tapes': tapes
        })