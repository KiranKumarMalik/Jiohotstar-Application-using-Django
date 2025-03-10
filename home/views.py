from django.shortcuts import render
from .models import *
from django.contrib.auth.models import auth

# Create your views here.
def home(request):
    bannerCard = BannerCard.objects.all()
    context = {
        'bannerCard': bannerCard,
    }
    return render(request, "Home/home.html", context)
