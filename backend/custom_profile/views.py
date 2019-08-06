from backend import settings

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from custom_profile.models import Profile
from custom_profile.serializers import ProfileSerializer
from custom_profile.forms import SignUpForm


class ProfileOverall(APIView):  # 자신의 프로필
    """
        본인 프로필 조회 및 수정

        ---
        # 내용
            - is_admin : 관리자 여부
            - student_id : 바코드에 있는 학생증 정보
            - class_id : 반 고유 코드 (아두이노 ID)
            - bio : 한줄소개. ex) 선린인터넷고등학교 1학년 3반
        # 주의 할 점
        구현상 미숙으로 patch를 할때에는 모든 parameter가 있어야함. 없을시에는 null값으로 들어가게 됨.  
        즉, is_admin, student_id, class_id, bio 가 요청시에 모두 parameter로 존재해야함.
    """
    def get(self, request):  # 프로필 조회
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except:
                Profile.objects.create(user=request.user)
                profile = Profile.objects.get(user=request.user)

            return Response(
                {
                    'is_admin': profile.is_admin,
                    'student_id': profile.student_id,
                    'class_id': profile.class_id,
                    'bio': profile.bio
                },
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except:
                Profile.objects.create(user=request.user)
                profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def sign_up(request):  # 회원가입
    """
        회원가입

        ---
        # 내용
            - username : 로그인시에 사용할 username
            - email : 사용자 정보로 들어갈 email
            - password1 : 패스워드 입력
            - password2 : 패스워드 확인
        # 주의 할 점
        password가 email 혹은 username과 너무 비슷하거나 단순할 경우 Django에서 자체적으로 계정 생성을 차단합니다.  
        이 경우에는 response에 어떤 부분이 문제인지 기술됩니다.
    """
    form = SignUpForm(request.POST)
    try:
        User.objects.get(email=request.data.get('email'))
        return Response({"email": "해당 이메일은 이미 존재합니다."},
                        status=status.HTTP_406_NOT_ACCEPTABLE)
    except User.DoesNotExist:  # 이메일이 중복이 아닐경우에
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Profile.objects.create(user=user)
            return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
