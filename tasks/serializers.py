from rest_framework import serializers
from .models import User, Task

# A serializer is important for apis to convert 
# incoming and outgoing messages 
# to adhere to a format that the api 
# works on 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
