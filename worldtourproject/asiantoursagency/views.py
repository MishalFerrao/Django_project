from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour

# Create your views here.
def index(request):
    tour = Tour.objects.all()
    context = {'tours':tour}
    return render(request,'tours/index.html',context)
