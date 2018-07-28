from django.conf.urls import url
from .views import UserList,UserDetail

urlpatterns = [
    url(r'^$',UserList.as_view(),name='usernames'),
    url(r'^(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
]
