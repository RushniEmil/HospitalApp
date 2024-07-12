from django.db import models

class Patient(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    Date_of_birth=models.DateField()
    address=models.TextField()
    phone=models.TextField()
    email=models.EmailField(max_length=50)
