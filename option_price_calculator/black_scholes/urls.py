from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='black_scholes-home'),
    path('eval/',views.eval,name='black-scholes-evaluation')
]