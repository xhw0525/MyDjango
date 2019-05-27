from rest_framework import serializers
from zxchat.models import ZXUserModel, ZXAutoReplyModel


class ZXUserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZXUserModel
        fields = ('username', 'phone', 'sex')
