from django.db import models
from django.urls import reverse

# Create your models here.

gender_choices=(('M','Male'),('F','Female'),('O','Others'),)

class Patient(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=gender_choices,default='Others')

    def get_absolute_url(self):
       return reverse("patientList")
    
    def __str__(self):
        return self.name
    
class PatientClinicalData(models.Model):
    Patient=models.OneToOneField(Patient,on_delete=models.CASCADE)
    height=models.IntegerField()
    weight=models.IntegerField()
    bloodPressure=models.IntegerField()
    heartRate=models.IntegerField()

    def get_absolute_url(self):
       return reverse("getPatientClinicalData",args=[self.Patient.id])

    def __str__(self):
        return self.Patient.name
