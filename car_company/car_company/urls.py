
"""car_company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from customers import views
from Administrator import views as aviews
from cars import views as cviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('signup/',views.signup),
    path('index/signup.html/',views.signup),
    path('index/login.html/',views.login),
    path('img/',views.img),
    path('index/login admin.html/',aviews.login_admin),
    path('index/login admin.html/customer_info.html',aviews.get_queryset),
    path('index/login admin.html/delete.html',aviews.delete_user),
    path('index/login admin.html/onecust.html',aviews.onecust),
    path('index/login admin.html/cars.html/',cviews.picupload),
    path('index/login admin.html/viewcars.html/',cviews.picget),
    path('index/login admin.html/editrate.html/',aviews.editrate),

 
    
     
    
]
if settings.DEBUG:
        urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

