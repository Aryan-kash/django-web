from django.shortcuts import render
from .models import customers

# Create your views here.
def signup(request):
   if request.method=='POST':
     if request.POST.get('username') and request.POST.get('password') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('age') and request.POST.get('gender'):
       post=customers()
       post.username=request.POST.get('username')
       post.password=request.POST.get('password')
       post.first_name=request.POST.get('first_name')
       post.last_name=request.POST.get('last_name')
       post.age=request.POST.get('age')
       post.gender=request.POST.get('gender')
       age1=int(request.POST.get('age'))
       if age1>18:
          post.save()
       else:
           return render(request,'UNSUCCESS.html')
   return render(request,'signup.html')

def login(request):
   if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=customers.objects.filter(username=username,password=password)
       if user:
         return render(request,'LOGGEDIN.html',{'user':user})
       else:
         return render(request,'UNSUCCESS.html')
       
   return render(request,'login.html')

def index(request):
   return render(request,'index.html')

def img(request):
   return render(request,'img.html')

   
