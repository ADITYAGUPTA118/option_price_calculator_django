from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='two_step-home'),
    path('eval/',views.eval,name='evaluation')
]