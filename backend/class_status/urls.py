from django.conf.urls import url
from class_status import views

urlpatterns = [
    url(r'^$', views.create_image),  # 프로필 정보를 얻거나 , 변경하는 라우트
]