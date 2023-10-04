from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy

# Create your views here.

class CreatePatientRecord(CreateView):
    model=models.Patient
    fields='__all__'

class PatientList(ListView):
    model=models.Patient
    
class PatientUpdate(UpdateView):
    model=models.Patient
    fields='__all__'

class PatientDelete(DeleteView):
    model=models.Patient
    success_url=reverse_lazy('patientList')

def getPatientClinicalData(request,pk):
    patient=models.Patient.objects.get(id=pk)
    if models.PatientClinicalData.objects.filter(Patient=patient.id).exists():
        record=models.PatientClinicalData.objects.get(Patient=patient.id)
    else:
        record=False
    return render(request,'patientsApp/patient_detail.html',{'patient':patient,'record':record})


class CreatePatientClinicalData(CreateView):
    model=models.PatientClinicalData
    fields=['height','weight','bloodPressure','heartRate']


    def form_valid(self, form):
        form.instance.Patient =models.Patient.objects.get(id=self.kwargs['pk']) 
        return super(CreatePatientClinicalData,self).form_valid(form)

    
class UpdatePatientClinicalData(UpdateView):
    model=models.PatientClinicalData
    fields=['height','weight','bloodPressure','heartRate']

class DeletePatientClinicalData(DeleteView):
        model=models.PatientClinicalData
        success_url=reverse_lazy('patientList')




