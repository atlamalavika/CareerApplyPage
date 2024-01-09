from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def home(request):
    apply_obj=User.objects.all()
    serializer=ApplySerializer(apply_obj,many=True)
    return Response({'status':200,'payload':serializer.data})
@api_view(['POST'])
def postData(request):
    apply_obj=User.objects.all()
    serializer=ApplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)