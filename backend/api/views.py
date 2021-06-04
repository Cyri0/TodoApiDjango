from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
import json

@api_view(['GET'])
def apiCommands(request):
    api_urls = {
        'Commands':'api/',
        'List':'api/task-list/',
        'Task by id':'api/task/<id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    print('Adatok:\n',serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def getTask(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    title = request.data['title']
    t = Task(title = title)
    t.save()
    return Response({'result':'Created!'})