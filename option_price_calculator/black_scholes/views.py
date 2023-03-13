from django.shortcuts import render
import scipy
from scipy.stats import norm
import math
# Create your views here.
def home(request):
    return render(request,'black_scholes/black_scholes.html')

def eval(request):
    S0=float(request.GET["S0"])
    K=float(request.GET["K"])
    r=float(request.GET["r"])
    T=float(request.GET["T"])
    Si=float(request.GET["Si"])
    d1=((math.log(S0/K)+(r+(math.pow(Si,2))/2)*T)/(Si*math.pow(T,0.5)))
    d2=((math.log(S0/K)+(r-math.pow(Si,2)/2)*T)/(Si*math.pow(T,0.5)))
    resc=S0*(norm.cdf(d1))-K*(math.pow(math.e,(-1)*r*T))*(norm.cdf(d2))
    return render(request,'black_scholes/result.html',{'result':resc})