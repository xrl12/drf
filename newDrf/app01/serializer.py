from rest_framework import serializers

from .models import Group, Student


class GroupSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Group
       fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'