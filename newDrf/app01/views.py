from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Student, Group
from .serializer import StudentSerializer, GroupSerializer


# Create your views here.

# def student_list(request, *args, **kwargs):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         data = JSONRenderer().render(students)
#         ser = StudentSerializer(data, many=True)
#         return HttpResponse(ser.data, content_type='applicaations/json', status=status.HTTP_200_OK, )
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         ser = StudentSerializer(data=data)
#         if ser.is_valid():
#             ser.save()
#             return HttpResponse(ser.data, content_type='applications/json', status=status.HTTP_201_CREATED)
#         return HttpResponse(ser.errors, content_type='applications/json', status=status.HTTP_400_BAD_REQUEST)


from rest_framework.viewsets import ModelViewSet
class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GroupViewset(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer