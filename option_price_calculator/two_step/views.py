from django.shortcuts import render
import math
# Create your views here.
def home(request):
    return render(request,'two_step/two_step.html')

def eval(request):
    S0=float(request.GET["S0"])
    K=float(request.GET["K"])
    r=float(request.GET["r"])
    u=float(request.GET["u"])
    d=float(request.GET["d"])
    T=float(request.GET["T"])
    p=((math.pow(math.e,r*(T/2))-d)/(u-d))
    fuu=max(S0*u*u-K,0)
    fud=max(S0*u*d-K,0)
    fdd=max(S0*d*d-K,0)
    res=(math.pow(math.e,(-1)*r*T))*(p*p*fuu + p*(1-p)*fud + (1-p)*(1-p)*fdd)
    return render(request,'two_step/result.html',{'result':res})