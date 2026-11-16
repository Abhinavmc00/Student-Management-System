from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from studApp.serializers import UserSerializer,StudentSerializer
from studApp.models import StudentModel
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter 
# Create your views here.


class UserRegistrationView(CreateAPIView):
    serializer_class=UserSerializer

class StudentRegistrationView(CreateAPIView):
    serializer_class=StudentSerializer

class StudentDataView(ListAPIView):
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=StudentModel.objects.all()

    filter_backends=[
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    ]

    filterset_fields=['course','name']
    search_fields=['name','course']
    Ordering_fields=['fees']

class StudentDataUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=StudentModel.objects.all()


class FeeStatus(ListAPIView):
    pass