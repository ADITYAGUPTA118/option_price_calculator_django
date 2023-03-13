from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home-home'),
    path('two_step/',include('two_step.urls')),
    path('n_step/',include('n_step.urls')),
    path('black_scholes/',include('black_scholes.urls'))
]