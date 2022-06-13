from django.urls import path,re_path
from . import views
# from rest_framework.routers import DefaultRouter
urlpatterns = [
    # 列表视图的路由
    re_path('^books/$', views.BookListAPIView.as_view()),
    re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailAPIView.as_view())
]
# router = DefaultRouter()  #可以处理视图的路由器
# router.register(r'books', views_bk.BookInfoViewSet)  #向路由器中注册视图集
#
# urlpatterns += router.urls
