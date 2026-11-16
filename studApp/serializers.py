from rest_framework import serializers
from django.contrib.auth.models import User
from studApp.models import StudentModel


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields="__all__"
        read_only_fileds=['joining_date','fees']

    # def validate(self, fees):
    #     if is_fee_paid!=pending
        
