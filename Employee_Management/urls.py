"""Employee_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('index/',views.login1, name='login'),
    path('logout/',views.logout1, name = 'logout1'),
    path('update/<int:pk>',views.update_profile.as_view(),name='update_profile'),
    path('leave/',views.Leave.as_view(), name ='leave1'),
    path('detail/',views.Employee_List.as_view(),name='empdetail'),
    path('todaybirthday/',views.today_birthday,name='todaybirthday'),
    path('upcoming/',views.upcoming_birthday,name='upcoming'),
    path('leavedetail/',views.view_leave,name='leave_detail'),
    path('manager_page/',views.manager_page, name='manager_page'),
    path('dashboard_page/',views.dashboard_page,name='dashboard_page')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
