from django.shortcuts import render
from . import forms

# Create your views here.
def userRegistration(request):
    form=forms.UserRegistrationForm()
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            # now the post data will be stored in form dict under cleaned_data key
            print(form.cleaned_data['firstName'])
    return render(request,'formsApp/userRegistration.html',{'form':form})
