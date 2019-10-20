from django.shortcuts import render, redirect
from django.http  import HttpResponse
# from django.views.generic import(ListView)
from .forms import NewsLetterForm, UpdatebioForm, NewImageForm
# from .models import Image, Profile, Review
from .models import Image,  Profile, Follow
from django.contrib.auth.forms import UserCreationForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    
    return render(request, 'welcome.html')



def search_users(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_by_users(search_term)
        message = f"{search_term}"

        return render(request, 'welcome.html',{"message":message,"profiles": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'welcome.html',{"message":message})
    
@login_required(login_url='/accounts/login/')
def profile(request,username=None):
    if not username:
        username = request.user.username
    try:
        images = Image.objects.filter(user_id=username)
    except DoesNotExist:
        raise Http404()
    
    return render (request, 'registration/profile.html', {'images':images, 'username': username})