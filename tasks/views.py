from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from django.http import JsonResponse
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def default_page(request):
    api_urls = {
        'Create Task': '/api/tasks/',
        'Assign Task': '/api/tasks/<int:task_id>/assign/',
        'Get Tasks for User': '/api/users/<int:user_id>/tasks/',
        'Create User': '/api/users/',
    }
    return Response(api_urls)

@api_view(['POST'])
def assign_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    users = request.data.get('users')
    if users:
        for user_id in users:
            try:
                user = User.objects.get(id=user_id)
                task.users.add(user)
            except User.DoesNotExist:
                return Response({'error': f'User with id {user_id} not found'}, status=status.HTTP_404_NOT_FOUND)
        task.save()
        return Response({'message': 'Task assigned to users'}, status=status.HTTP_200_OK)
    return Response({'error': 'No users provided'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tasks_for_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    tasks = user.tasks.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
