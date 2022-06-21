from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookInfoModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import BookInfo
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from apps.utils.filters import BookFilter

class StandardPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


"""以下是继承APIView的视图"""
class BookListAPIView(APIView):
    '''
    列表视图
    '''

    def get(self, request):
        # 查询所有图书接口

        # 1、查询出所有图书模型
        books = BookInfo.objects.all()
        # serializer = BookInfoModelSerializer(instance=books, many=True)
        # # 指定过滤后端为排序
        # filter_backends = [OrderingFilter]
        # # 指定排序字段
        # ordering_fields = ('bread', 'btitle')
        # filter_class = BookFilter  # 过滤类
        filter_fields = ('btitle', 'bread')
        # 指定自定义分页器
        pagePagination = StandardPageNumberPagination()
        pagedata = pagePagination.paginate_queryset(books, request)  # 必须传两个参数,第一个queryset对象要分页的所有数量，第二个参数request
        serializer = BookInfoModelSerializer(instance=pagedata, many=True)
        pageresponse = pagePagination.get_paginated_response(serializer.data)

        return Response(pageresponse.data)
        # return Response(serializer.data)

    def post(self, request):
        """
        新增
        """
        #获取前端传入的请求体数据
        data = request.data
        #创建序列器进行返序列化
        serializer = BookInfoModelSerializer(data=data)
        #调序列号器的is_valid 进行校验
        serializer.is_valid(ralse_exception=True)
        #调用序列化器的save方法进行create方法
        serializer.save()
        #相应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookDetailAPIView(APIView):
    '''
    详情视图
    '''

    def get(self, request, pk):
        # 查询pk指定的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_CREATED)
#创建序列器进行返序列化
        serializer = BookInfoModelSerializer(instance=book)
        # 3、响应
        return Response(serializer.data)

    def put(self, request, pk):
        """
        修改图书信息
        路由： PUT  /books/<pk>
        """
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_CREATED)
        #获取前端传入的请求体数据
        #创建序列化器进行返序列化
        ser = BookInfoModelSerializer(instance=book, data=request.data)
        #校验
        ser.is_valid(raise_exception=True)
        ser.save()
        #相应
        return Response(ser.data)


    def delete(self, request, pk):
        """
        查询pk所指定的模型对象
        """
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_CREATED)

        book.delete()

        return Response(status=status.HTTP_204_CREATED)

