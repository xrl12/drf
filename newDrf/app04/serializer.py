import re

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11, min_length=11, required=True)
    # pwd2 = serializers.CharField(max_length=20, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            # 在序列话的时候必须传一个密码，在反序列化不需要传入
            'pwd': {'write_only': True}
        }

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        representation['gender'] = instance.get_gender_display()
        return representation
    #
    # def validate_phone(self, phone):  # (对单个进行验证)
    #
    #     result = re.match(r'1[3456789]\d{9}', phone)
    #     phones = User.objects.filter(phone=phone)
    #     if phones:
    #         raise serializers.ValidationError('手机号已经存在了')
    #     if not result:
    #         raise serializers.ValidationError('手机号不合法')
    #     return phone
    #
    # def validate(self, attrs):
    #     if not attrs.get('pwd') == attrs.get('pwd2'):
    #         raise serializers.ValidationError('两次密码输入不一样')
    #     if 'pwd2' in attrs:
    #         attrs.pop('pwd2')
    #     return attrs
