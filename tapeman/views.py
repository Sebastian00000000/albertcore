from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from .models import *

# Create your views here.


class TapeView(View):
    def get(self, request, *args, **kwargs):
        ...