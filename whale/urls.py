"""
URL configuration for whale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from whale.views import index
from blog.views import post_list, post_detail

# 아래 2줄은 media 파일을 보기위한 링크를 추가해 주기 위하여 중요하다.
# 사실상 메인프로젝트의 settings.py에 설정된 것을 가져오는 것
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("posts/", post_list),
    # 특히 이 표현이 중요하다. 각 id값에 맞는 링크 설정
    path("posts/<int:post_id>/", post_detail)
]

# media를 추가 하기 위한 세팅
urlpatterns += static(
    # url의 접두어가 media_url일때는 정적 파일을 돌려준다.
    prefix=settings.MEDIA_URL,
    # 돌려줄디렉토리는 MEDIA_ROOT를 기준으로 해준다는 것
    document_root= settings.MEDIA_ROOT   
)