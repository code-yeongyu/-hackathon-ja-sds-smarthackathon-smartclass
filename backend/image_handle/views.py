import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from image_handle.serializers import ImageSerializer
from django.shortcuts import get_object_or_404
from image_handle.models import Image
#import image_handle.yolo as yolo


@api_view(['POST'])
def create_image(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        path = "./" + get_object_or_404(Image,
                                        pk=serializer.data['id']).image.url
        return Response(status=HTTP_200_OK)
        #return Response(yolo.AnyBodyHere(path), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)