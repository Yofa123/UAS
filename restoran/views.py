from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Member

def members(request):
    mem=Member.objects.all()
    return render(request,'members.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['email']
    mem=Member(firstname=x,lastname=y,email=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['email']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.email=z
    mem.save()
    return redirect("/")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())
def service(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())
def team(request):
    template = loader.get_template('team.html')
    return HttpResponse(template.render())
def testimonial(request):
    template = loader.get_template('testimonial.html')
    return HttpResponse(template.render())
def sukses(request):
    template = loader.get_template('sukses.html')
    return HttpResponse(template.render())
def heyy(request):
    template = loader.get_template('heyy.html')
    return HttpResponse(template.render())
