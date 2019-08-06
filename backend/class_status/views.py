from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from class_status.serializers import StatusSerializer
from class_status.models import Status
import class_status.yolo as yolo


@swagger_auto_schema(methods=['post'], request_body=StatusSerializer)
@api_view(['POST'])
def create_image(request):
    """
    상태 업로드 하는 라우터

    ---
    arduino_id: 아두이노 id
    image: form-data 형식으로 된 image
    gas_quality: float 형식으로 된 아두이노 gas 모듈의 값
    air_quality: float 형식으로 된 아두이노 pm2.5 모듈의 값
    """
    serializer = StatusSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        path = "./" + get_object_or_404(Status,
                                        pk=serializer.data['id']).image.url
        return Response(yolo.AnyBodyHere(path), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)