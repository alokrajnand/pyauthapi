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
        
        #check if phone number is provided
        #check id name is given              
        #check if a valid email id is provided 
        #check if date of birth is given

        #if all the above condition are valid check phone number exists in the myuser table or not
                #if phone number exists you are all ready registered  please login or go to forget password 
                # if phone number does not exists  then send the otp and varification link to the email address and redirct the user to the varification page



        # Check if varification is success full 
            # check if phone varification is ok
            # check if email varification is ok
            # if both the varification is ok then register the user and redirect to the login page         


        # this will happen only when the phone otp and mail id varification will be done 
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        
        
        return JsonResponse(serializer.errors, status=400)
