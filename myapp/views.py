from django.contrib.auth import authenticate
from django.shortcuts import render, redirect,reverse
from rest_auth.views import LoginView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.views.generic.edit import UpdateView,CreateView
from .models import *
from django.views.generic.list import ListView
from datetime import date
import datetime
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin







# Create your views here.

def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return render(request,'login.html')
        else:
            return render(request, 'index.html', {'form': form})
    else:
        form = register_form(request.POST)
        return render(request, 'index.html', {'form': form})

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            if user.is_staff== False:
                login(request,user)
                return render(request, 'dashboard.html', {'user': user})
            else:
                login(request, user)
                return render(request,'manager.html',{'user':user})
        else:
            return render(request,'login.html',{'error':'invalid username or password'})
    else:
        return render(request, 'login.html')

@login_required(login_url='login1')
def logout1(request):
    logout(request)
    return redirect(login1)

class update_profile(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    template_name = 'update_profile.html'
    model = emplyee_details
    fields = ['mobile','dob','current_profile','degination','resume']

    def get_success_url(self):
        return reverse(dashboard_page)

class Leave(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = leave_request
    template_name = 'leave.html'
    fields = ['duration_from','duration_to','leave_msg']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse(dashboard_page)

class Employee_List(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = emplyee_details
    paginate_by = 10
    template_name = 'empdetail.html'
    
@login_required(login_url='login1')
def today_birthday(request):
    datetime_now = timezone.now()
    now_day, now_month = datetime_now.day, datetime_now.month
    data = emplyee_details.objects.filter(dob__day=now_day, dob__month=now_month)
    return render(request,'manager.html',{'data':data})

@login_required(login_url='/login/')
def upcoming_birthday(request):
    datetime_now = timezone.now()
    datetime_tomorrow = datetime_now + timedelta(days=1)
    tomorrow_day, tomorrow_month = datetime_tomorrow.day, datetime_tomorrow.month
    data1 = emplyee_details.objects.filter(dob__day=tomorrow_day, dob__month=tomorrow_month)
    return render(request,'comingbirth.html',{'data1':data1})

@login_required(login_url='/login/')
def view_leave(request):
    data = leave_request.objects.all()
    return render(request,'leave_detail.html',{'data':data})

@login_required(login_url='/login/')
def manager_page(request):
    return render(request,'manager.html')

@login_required(login_url='/login/')
def dashboard_page(request):
    return render(request,'dashboard.html')

