from django.http import JsonResponse

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from noticeboard.models import Article
from noticeboard.serializers import ArticleSerializer


class ArticleList(generics.ListAPIView, APIView):
    """
        선생님용 게시판

        ---
        # 내용
            - content: 게시글 내용
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request):  # 작성자 이름 자동추가 기능을 위해 post용 뷰 분리
        if request.user.is_authenticated:  # 사용자가 인증 되었을경우
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(writer=request.user)  # 작성자 요청자로 설정
                return JsonResponse(serializer.data,
                                    status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)  # 폼에 오류가 있을 경우
        return Response(status=status.HTTP_401_UNAUTHORIZED)  #인증되지 않았을 경우


class ArticleDetail(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )