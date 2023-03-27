from django.shortcuts import render
from .models import admin_user
from customers.models import customers
from cars.models import image
# Create your views here.
def login_admin(request):
   if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=admin_user.objects.filter(username=username,password=password)
       if user:
         return render(request,'ADMINLOGGEDIN.html',{'user':user})
       else:
         return render(request,'UNSUCCESS.html')
       
   return render(request,'login admin.html')

def get_queryset(request):
      records=customers.objects.all()
                        
      return render(request,'customer_info.html',{'records':records})

def car_details(request):
   return render(request,'car_details.html')

def delete_user(request):
       if request.method=='POST':
        username=request.POST.get('username')
         
        delete =  customers.objects.get(username=username)
        delete.delete()


       return render(request,'delete.html')

def onecust(request):
   if request.method=='POST':
     username=request.POST.get('username') 
     records=customers.objects.filter(username=username)
     return render(request,'customer_info.html',{'records':records})
   return render(request,'onecust.html')

def editrate(request):
   if request.method=='POST' and 'submit' in request.POST:
     global Car_Id
     Car_Id=request.POST.get('Car_Id')
     cardet=image.objects.filter(Car_Id=Car_Id)
     return render(request,'editrate.html',{'Car_Id':Car_Id,'cardet':cardet})
   
   if request.method=='POST'and 'edit' in request.POST:
     Rate_perday=request.POST.get('Rate_perday')
     image.objects.filter(Car_Id=Car_Id).update(Rate_perday=Rate_perday)
     
     
   return render(request,'editrate.html')

