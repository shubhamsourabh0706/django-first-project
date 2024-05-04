from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def empform(request):
    return render(request,'blog/empform.html')

def empdata(request):
    btn=request.GET.get('sub')
    if btn=='Submit':
        #id=request.GET.get('eid')
        #name=request.GET.get('ename')
        #designation=request.GET.get('edesi'),
        #location=request.GET.get('eloc'),
        salary=request.GET.get('esal')
        data=Employee(esal=salary)
        data.save()
        param={'msg :' 'Record Inserted'}
        return render(request,'blog/empform.html',param)


    if btn=='Display':
        pass