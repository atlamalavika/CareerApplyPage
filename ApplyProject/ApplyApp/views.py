from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
@api_view(['GET'])
def home(request):
    apply_obj=User.objects.all()
    serializer=ApplySerializer(apply_obj,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def postData(request):
    apply_obj=User.objects.all()
    serializer=ApplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        subject = 'Confirming job application.'
        message = f'Hi {serializer.data["name"]}, thank you for applying for the job.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [serializer.data["mailid"], ]
        send_mail( subject, message, email_from, recipient_list )
    return Response(serializer.data)