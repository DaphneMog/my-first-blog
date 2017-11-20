
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^A', views.a, name='a_view'),
    url(r'^B', views.b, name='b_view'),
    url(r'^C', views.c, name='c_view'),
    url(r'^about_me', views.about, name='about_view'),
]
