from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('whyus/', views.whyus, name='whyus'),
    path('contactus/', views.contactus, name='contactus'),
]
