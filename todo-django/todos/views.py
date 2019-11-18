from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializers


@api_view(['GET'])
# Create your views here.
def todo_index_create(request):
    todos = Todo.objects.all()
    serializers = TodoSerializers(todos, many=True)
    return Response(serializers.data)