from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.About,name="About"),
    path('Adddonar/',views.Adddonar,name="Adddonar"),
    path('Contactus/',views.Contactus,name="Contactus"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('loginPage/',views.LoginPage,name="LoginPage"),
    path('Needblood/',views.Needblood,name="Needblood"),
    #path('logout/',LogoutView.as_view(),name="logout"),
]
'''
from django.conf.urls import url, include 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blooddonationsystem import views as user_views
urlpatterns = [
url(r'^admin/', admin.site.urls),
url('contact/',user_views.ContactView,name='contact'),
url('adddonor/',user_views.AddView,name='adddonor'), 
url('feedback/',user_views.FeedbackView,name='feedback'), 
url('login/',auth_views.LoginView.as_view(template_name='blooddonationsystem /LoginPage.html'),name='login'), 
url('profile/',user_views.NeedView,name='needblood'), 
url(r'^', include('blooddonationsystem.urls'))
'''