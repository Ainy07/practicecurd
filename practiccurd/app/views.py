from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http.response import HttpResponse
from . models import Employee
# Create your views here.
def signup(request):
    return render(request,'signup.html')

#create signup form
def signup_data(request):
    if request.method == 'POST':
         name = request.POST['name']
         email = request.POST['email']
         password = make_password(request.POST['password'])
         company = request.POST['company']
         areacode = request.POST['areacode']
         contact = request.POST['contact']
         subject = request.POST['subject']
         if Employee.objects.filter(email=email).exists():
             messages.error(request, "Email Already Exists")
             return redirect("/")
         elif Employee.objects.filter(contact=contact).exists():
             messages.error(request,"Contact Already Exists")
             return redirect("/")
         else:
             Employee.objects.create(name=name,email=email,password=password,company=company
                                     ,areacode=areacode,contact=contact,subject=subject
                                     )
         return redirect("/login/")    


def login(request):
    return render(request,'login.html')

#create login form
def login_data(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if Employee.objects.filter(email=email).exists():
            obj = Employee.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect("/table/")
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Email is not registered")
                

#create table data
def table(request):
    data = Employee.objects.all()
    return render(request,'table.html',{"data":data})

#create Edit button
def update(request,uid):
    res = Employee.objects.get(id=uid)
    return render(request,"update.html" ,{'user':res})



#use update data
def update_data(request):
    if request.method == 'POST':
         uid = request.POST['uid']
         name = request.POST['name']
         email = request.POST['email']
         company = request.POST['company']
         areacode = request.POST['areacode']
         contact = request.POST['contact']
         subject = request.POST['subject']
         Employee.objects.filter(id=uid).update(name=name,email=email,company=company
                                                   ,areacode=areacode,contact=contact
                                                   ,subject=subject)
         return redirect("/table/")
     

#craete delete button
def delete(request,pk):
    use = Employee.objects.filter(id=pk).delete()
    return redirect("/table/")
         
             