
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from .serializers import MemberSerializer
from .models import MemberV0
# Create your views here.
'''
@api_view(['POST'])
@parser_classes([JSONParser])
def Signup(request):
    data = JSONParser().parse(request)
    # data is not empty
    # print(type(data)): dict
    serializer = MemberSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)'''
class Members(APIView):
    @staticmethod
    def post(request):
        data = request.data['body']
        # print(data)
        # print(type(data))
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'welcome {serializer.data.get("name")}'}, status=201)
        return Response(serializer.errors, status=400)
    def get(self, request):

        pass
class Member(APIView):
    def post(self, request):
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = self.get_object(pk)
        if user_input_password == member.password:
            return Response({'result': 'you are logged in'}, status=201)
        return HttpResponse(status=104)
        # print(type(member)): when pk is correct, <class 'member.models.MemberVO'>
        # print(member.pk) = print(member.username)
    @staticmethod
    def get_object(pk):
        try:
            return MemberV0.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404


@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        serializer = MemberSerializer()
        if serializer.is_valid():

            serializer.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)