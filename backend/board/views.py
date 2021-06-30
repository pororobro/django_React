from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from .serializers import BoardSerializer
from .models import BoardV0
from icecream import ic
# Create your views here.

class Boards(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)
@csrf_exempt
def member_list(request):
    if request.method == 'GET':
        serializer = BoardSerializer()
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)