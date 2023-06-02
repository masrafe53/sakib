from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    MainOffer = offer.objects.all()
    Alloffers = AllOffer.objects.all()
    heads = head.objects.all()
    dict = {
        "MainOffer":MainOffer , "Alloffers":Alloffers,"heads":heads
    }
    return render(request,'index.html',context=dict)