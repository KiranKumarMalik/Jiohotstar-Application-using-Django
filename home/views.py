from django.shortcuts import render
from .models import *
from django.contrib.auth.models import auth

# Create your views here.
def home(request):
    bannerCard = BannerCard.objects.all()
    card = Card.objects.all()
    context = {
        'bannerCard': bannerCard,
        'card': card,
    }
    return render(request, "Home/home.html", context)
