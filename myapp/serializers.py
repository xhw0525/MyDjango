from rest_framework import serializers
from myapp.models import MyUserModel, MyChatModel


class MyUserModelSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(help_text='用户名')

    class Meta:
        model = MyUserModel
        fields = '__all__'
        # fields = ('username', 'phone', 'sex')
