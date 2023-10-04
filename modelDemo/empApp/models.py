from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    salary=models.FloatField(null=True)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.firstName
    
# Many to many starts here

class Programmer(models.Model):
    name=models.CharField(max_length=30,null=True)
    sal=models.FloatField(null=True)

    def __str__(self):
        return self.name



class Project(models.Model):
    name=models.CharField(max_length=30,null=True)
    programmers=models.ManyToManyField(Programmer)

    def __str__(self):
        return self.name

# Many to many ends here


# one to many starts here

class Customer(models.Model):
    name=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    number=models.CharField(max_length=10,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return self.number

# one to many ends here




# one to one starts here

class Person(models.Model):
    name=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

class licenseNumber(models.Model):
    licenseNumber=models.CharField(max_length=10,null=True)
    Person=models.OneToOneField(Person,on_delete=models.CASCADE)

    def __str__(self):
        return self.licenseNumber

# one to one ends here