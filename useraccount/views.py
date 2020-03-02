from django.shortcuts import render
# this is to send response to client
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # to resolve csrf issue
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response


# model and serializer import
from .serializer import *
from .models import *


@csrf_exempt
def UserViewSet(request, format=None):

    if request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = MyUserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
