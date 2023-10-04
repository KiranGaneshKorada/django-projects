from django import forms
# in order to use inbuilt validators import the below package
from django.core import validators

class UserRegistrationForm(forms.Form):
    firstName=forms.CharField(validators=
                              [validators.MinLengthValidator(5),
                               validators.MaxLengthValidator(20)])
    lastName=forms.CharField()
    email=forms.EmailField()
    GENDER=[('male','MALE'),('female','FEMALE')]
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)

"""

    # single clean method to do all custom validations after completion of default validations under one place

    def clean(self):
        user_cleaned_data=super().clean() 
        # obtaining data as dict which went through default alidations
        inputed_firstName=user_cleaned_data['firstName']
        if len(inputed_firstName)>20:
            raise forms.ValidationError('length exceeded 20')
        inputedemail=user_cleaned_data['email']
        if inputedemail.find('@gmail.com')==-1:
            raise forms.ValidationError('enter email with crct format')
        
        # no need to return cleaned data to view as below it is returned defaultly



"""

""" INDIVIDUAL CUSTOM VALIDATION

    # custom validations (custom validations are invoked after completion of its default validations)

    def clean_firstName(self):
        inputed_firstName=self.cleaned_data['firstName']
        if len(inputed_firstName)>20:
            raise forms.ValidationError('length exceeded 20')
        return inputed_firstName 
        # returning data to view for further processing like save(),update()etc..,
    

    def clean_email(self):
        inputedemail=self.cleaned_data['email']
        if inputedemail.find('@gmail.com')==-1:
            raise forms.ValidationError('enter email with crct format')
        return inputedemail

"""


