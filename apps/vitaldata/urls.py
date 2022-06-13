from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter
urlpatterns = [
    # 列表视图的路由
    # re_path('^$', views.hello),
    # re_path('^data/$', views.VitalListView.as_view()),
    # re_path(r'^data/(?P<pk>\d+)/$', views.DetailView.as_view())
]
router = DefaultRouter()  #可以处理视图的路由器
router.register(r'data', views.VitalDataViewSet)  #向路由器中注册视图集

urlpatterns += router.urls
