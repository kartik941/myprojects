from django.shortcuts import render ,HttpResponse
from home.models import *

def index(request):

    return render(request,'index.html',{"products":product.objects.all()})

# Create your views here.
