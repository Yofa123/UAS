from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('sukses', views.sukses, name='sukses'),
    path('heyy', views.heyy, name='heyy'),
    path('members',views.members,name="members"),
    path('add',views.add,name="add"),
    path("addrec",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec")
]