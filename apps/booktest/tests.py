from django.test import TestCase

# Create your tests here.
import os,django,sys
sys.path.append('./')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restframeworkdemo.settings")# project_name 项目名称
django.setup()
from booktest.models import BookInfo


# book1 = BookInfo.objects.create(
#     btitle='西游记',
#     bpub_date='1997-11-11'
# )
#
# book2 = BookInfo.objects.create(
#     btitle='三国演义',
#     bpub_date='1998-11-11'
# )
#
# book3 = BookInfo.objects.create(
#     btitle='红楼梦',
#     bpub_date='1999-11-11'
# )
for i in range(1000):
    # print('红楼梦'+str(i))
    BookInfo.objects.create(
        btitle='红楼梦'+str(i),
        bpub_date='1999-11-11')

