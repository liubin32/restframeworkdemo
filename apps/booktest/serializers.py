from rest_framework import serializers
from .models import BookInfo


class BookInfoModelSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""

    class Meta:
        model = BookInfo
        # 使用fields来明确字段，__all__表名包含所有字段
        # fields = '__all__'
        fields = ('btitle', 'bpub_date', 'bread', 'bcomment', 'is_delete')
        # 通过read_only_fields指明只读字段，即仅用于序列化输出的字段
        # read_only_fields = ('btitle', 'bpub_date', 'bread', 'bcomment', 'is_delete')
