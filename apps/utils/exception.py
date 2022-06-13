from rest_framework.views import exception_handler
from rest_framework.views import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)
    print(exc)

