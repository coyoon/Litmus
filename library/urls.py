from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'library^$', views.color_list, name='color_list'),
]