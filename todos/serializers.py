from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      # The model it will serialize
      model = Todo
      # The fields that should included in the serialized output
      fields = ['id', 'subject', 'details']