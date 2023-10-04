from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Student
from django.urls import reverse_lazy

# Create your views here.

class StudentListView(ListView):
    model=Student
    # default template_name is student_list.html(sub folder name is appname in templates folder)
    # default context_object_name is student_list
    # in order to custom those simply use above attributes and assign urself


class StudentDetailView(DetailView):
    model=Student
    # default template name is student_detail.html(sub folder name is appname in templates folder)
    # default context_object_name is student
    # in order to custom those simply use above attributes and assign urself


class StudentCreateView(CreateView):
    # in function based views we should create a form but here CreateView creates for us
    # default template name is student_form.html(sub folder name is appname in templates folder)
    # default context_object_name is form
    # in order to custom those simply use above attributes and assign urself

    model=Student
    fields=['name','age','marks']

    # after the form is submitted the Student model calls its get_absolute_url() method to redirect to requested page refer models.py


# CREATE VIEW AND UPDATE VIEW USES THE SAME FORM MODEL_FORM.HTML

# use reverse funtn when redirection is done after saving data in models.py(recomended approach)

# use reverse_lazy funtn when success redirection is done in views.py inorder to avoid run-time Exceptions

# models approach is recomended for CREATE , UPDATE . but not possible for DELETE view, so we do using views approach of redirecting.


class StudentUpdateView(UpdateView):
    model=Student
    fields=['age','marks']


class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('studentsList')

    # default template name is student_confirm_delete.html(sub folder name is appname in templates folder)

    # default context_object_name is student

