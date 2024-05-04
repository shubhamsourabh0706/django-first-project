from django.shortcuts import render

def home(request):
    return render(request, 'myApp/home.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request, 'myApp/contact.html')

def form_data(request):
    fname=request.GET.get('fname')
    lname=request.GET.get('lname')
    email=request.GET.get('email')
    password=request.GET.get('password')
    mobile=request.GET.get('mobile')
    #print(fname,lname,email,password,mobile)
    params = {"fname" : fname , "lname" : lname, "email":email, "password":password, "mobile":mobile}
    return render(request, 'myApp/form_data.html',params)
