from django.shortcuts import render

# Create your views here.
from django .core. files. storage import FileSystemStorage
from django. conf import settings
from. models import image

def picupload(request):
       if request.method=='POST' and request.FILES['myfile']:
         post=image()
         post.Car_Id=request.POST.get('Car_Id')
         post.Car_name=request.POST.get('Car_name') 
         post.Car_type=request.POST.get('Car_type') 
         post.Rate_perday=request.POST.get('Rate_perday')
         post.myfile=request.FILES['myfile']
         myfile=request.FILES['myfile']
         fs=FileSystemStorage()
         filename=fs.save(myfile.name,myfile)
         uploaded_file_url=fs.url(filename)
         post.img_url= uploaded_file_url
         post.save()
       return render(request, 'cars.html' )  

def picget(request):
      if request.method=='GET':
         allrecords=image.objects.all()
                        
      return render(request,'viewcars.html',{'allrecords':allrecords, 'media_url':settings.MEDIA_URL})
