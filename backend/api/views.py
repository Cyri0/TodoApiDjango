from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiCommands(request):
    api_urls = {
        'Commands':'api/',
        'List':'api/task-list/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    print('Adatok:\n',serializer.data)
    return Response(serializer.data)