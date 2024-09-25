from rest_framework import serializers
from .models import Products
from account.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Products
        fields = "__all__"

    def to_representation(self, instance):
        data= super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data
        return data
    
    def validate(self, obj):
        obj['user'] = self.context['request'].user
        return obj 