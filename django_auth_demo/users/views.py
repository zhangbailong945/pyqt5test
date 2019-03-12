from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied


# Create your views here.

UserModel=get_user_model()

def auth_premission_required(perm):


def register(request):

    redirect_to=request.POST.get('get',request.GET.get('next',''))

    if request.method=="POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    
    return render(request,'users/register.html',context={'form':form,'next':redirect_to})


def index(request):
    return render(request,'index.html')