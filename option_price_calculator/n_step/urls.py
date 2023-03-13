from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='n_step-home'),
    path('eval/',views.eval,name='n_step_eval')
]