"""
URL configuration for Hospital project.

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
from django.contrib import admin
from django.urls import path
from hospitalmanagement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('log_in/',views.log_in,name='log_in'),
    path('logout_admin/',views.logout_admin,name='logout_admin'),
    path('index/',views.index,name='index'),
    path('add_Doctor/',views.add_doctor,name='add_doctor'),
    path('remove_doctor/',views.remove_doctor,name='remove_doctor'),
    path('remove_doctor/<id>/',views.remove_doctor,name='remove_doctor'),
    path('view_doctor/',views.view_doctor,name='view_doctor'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('remove_patient/',views.remove_patient,name='remove_patient'),
    path('remove_patient/<id>/',views.remove_patient,name='remove_patient'),
    path('view_patient/',views.view_patient,name='view_patient'),
    # path('add_appointment/',views.add_appointment,name='add_appointment'),
    # path('remove_appointment/<id>/',views.remove_appointment,name='remove_appointment'),
    # path('view_appointment/',views.view_appointment,name='view_appointment'),
]
