from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import mail_admins
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *
import datetime


def dashboard(request):
    doctor = request.user.doctor

    context = {
        'doctor': doctor
    }
    return render(request, 'doctor_dashboard.html', context)
