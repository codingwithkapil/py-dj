from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('contacts',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('dark',views.darkmod, name='dark'),
]