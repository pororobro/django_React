# Create your views here.
# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from member.serializers  import MemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic
from rest_framework.parsers import JSONParser

class Members(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)

class Member(APIView):
    pass



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