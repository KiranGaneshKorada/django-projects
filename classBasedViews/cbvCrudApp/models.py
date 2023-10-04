from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    marks=models.IntegerField()

    # after successful save, below method is called, and  it can also be done in views.py using succes_url by using reverse_lazy method but this approach is recomended for CREATE , UPDATE . but not possible for DELETE view, so we do using views approach of redirecting.

    def get_absolute_url(self): # url inside reverse funtn is called success url

        # for redirecting page 
        return reverse("studentsList")
    
        # for redirecting page that need id or some value to redirect
        # return reverse("studentdetail", kwargs={"pk": self.pk})
    

