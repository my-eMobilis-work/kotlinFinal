
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('service/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('my_service/', views.my_service, name='my_service'),
    path('appointment/', views.appointment, name='appointment'),
    path('show_appointments/', views.show_appointments, name='show_appointments'),
    path('appoint_edit/<int:id>', views.edit_appointment, name='edit_appointment'),
    path('update_appointment/<int:id>', views.update_appointment, name='update_appointment'),
    path('appoint_delete/<int:id>', views.delete_appointment),
    path('contact/', views.contact, name='contact'),
    path('show_contacts/', views.show_contacts, name='show_contacts'),
    path('contact_delete/<int:id>', views.delete_contact),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('show_images/', views.show_images, name='show_images'),
    path('image_delete/<int:id>', views.image_delete),

    path('', views.register, name='register'),
    path('login/', views.login, name='login'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]
