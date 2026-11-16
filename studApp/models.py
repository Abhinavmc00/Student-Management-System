from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    course=models.CharField(max_length=80)
    fees=models.DecimalField(max_digits=10,decimal_places=2,default="20000")
    joining_date=models.DateField(default="2027-10-29")
    # student=models.ForeignKey(User,on_delete=models.CASCADE,related_name="student_profile")
    is_fee_paid=models.BooleanField()


