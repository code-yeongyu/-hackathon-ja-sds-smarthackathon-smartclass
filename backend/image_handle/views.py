import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from image_handle.serializers import ImageSerializer


@api_view(['POST'])
def create_image(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # image handling logic
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)