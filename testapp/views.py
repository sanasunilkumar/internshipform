from django.shortcuts import render
from . import forms
import datetime
from testapp.models import Empmodel
# Create your views here.
def Empout(request):
    emp=Empmodel.objects.all()
    return render(request,'testapp/wow.html',{'emp':emp})
def Endview(request):
    return render(request,'testapp/demo.html')
def Empview(request):
    date=datetime.datetime.now()
    form=forms.Empform()
    if request.method=='POST':
        form=forms.Empform(request.POST)
        if form.is_valid():
            form.save()
            return Endview(request)
    context = {'form': form, 'date': date}
    return render(request, 'testapp/home.html', context)
def Empmain(request):
    date=datetime.datetime.now()
    return render(request,'testapp/main.html',{'date':date})
