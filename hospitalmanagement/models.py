from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=200)
    mobile=models.IntegerField()
    special=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

# declaring a Student Model
GENDER_CHOICES = (
    ("1", "male"),
    ("2", "female"),
  
)
      
class Patient(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=20, choices=GENDER_CHOICES,default='1') 
    mobile=models.IntegerField()
    address=models.CharField(max_length=200)  
    def __str__(self):
        return self.name 

class Appointment(models.Model):
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return self.Doctor.Name+self.Patient.name