"""zero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

정규표현식(Regex)

URL패턴 만드는 방법이 궁금하다면, 다음 표기법을 확인하세요. 이 중 몇 가지 규칙만 사용할 거에요.

^ : 문자열이 시작할 떄
$ : 문자열이 끝날 때
\d : 숫자
: 바로 앞에 나오는 항목이 계속 나올 때
() : 패턴의 부분을 저장할 때
이외에도 문자열을 이용해 url을 만들 수 있어요.

http://www.mysite.com/post/12345/라는 사이트가 있다고 합시다. 여기에서 12345는 글 번호를 의미합니다.

뷰마다 모든 글 번호을 일일이 매기는 것은 정말 힘들죠. 정규표현식으로 url패턴을 만들어 숫자값과 매칭되게 할 수 있어요. 이렇게 말이죠. ^post/(\d+)/$. 어떤 뜻인지 하나씩 살펴봅시다.

^post/ : url이(오른쪽부터) post/로 시작합니다.
(\d+) : 숫자(한 개 이상)가 있습니다. 이 숫자로 조회하고 싶은 게시글을 찾을 수 있어요.
/ : /뒤에 문자가 있습니다.
$ : url 마지막이 /로 끝납니다.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url(r'', include('library.urls')),
    
]
