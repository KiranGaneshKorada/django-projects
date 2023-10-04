"""
URL configuration for patientClinicalRecord project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientList.as_view(), name='patientList'),

    path('addPatient/', views.CreatePatientRecord.as_view(), name='createpatientrecord'),

    path('patientUpdate/<int:pk>',views.PatientUpdate.as_view(),name='patientUpdate'),

    path('patientDelete/<int:pk>',views.PatientDelete.as_view(),name='patientDelete'),

    path('getPatientClinicalData/<int:pk>', views.getPatientClinicalData, name='getPatientClinicalData'),

    path('addpatientclinicaldata/<int:pk>', views.CreatePatientClinicalData.as_view(), name='addpatientclinicaldata'),

    path('updatePatientClinicalData/<int:pk>',views.UpdatePatientClinicalData.as_view(),name='updatePatientClinicalData'),

    path('deletePatientClinicalData/<int:pk>',views.DeletePatientClinicalData.as_view(),name='deletePatientClinicalData'),

]
