from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status
from .models import  User
from .serializer import UserSerializer


@api_view(['GET'])
def get_user(request):
    Users = User.objects.all()
    serializer = UserSerializer(Users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serialzer = UserSerializer(data= request.data)
    if serialzer.is_valid():
        serialzer.save()
        return Response(serialzer.data, status=status.HTTP_201_CREATED)
    return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DataNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

