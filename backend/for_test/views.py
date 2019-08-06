from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test(request):
    return Response({'ok': request.GET['id']}, status=status.HTTP_200_OK)
