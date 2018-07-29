from django.conf.urls import url
from .views import ProductList,ProductDetail,ProductListAPI,ProductConditionList,ProductConditionDetail

urlpatterns = [
    url(r'^$',ProductList.as_view(),name='productlist'),
    url(r'^(?P<pk>[0-9]+)/$',ProductDetail.as_view(),name='ProductDetail'),
    url(r'^search/$',ProductListAPI.as_view(),name='searchstuff'),
    url(r'^condition/$',ProductConditionList.as_view(),name='ProductCondition'),
    url(r'^condition/(?P<pk>[0-9]+)/$',ProductConditionDetail.as_view(),name='ProductDetail'),

]
