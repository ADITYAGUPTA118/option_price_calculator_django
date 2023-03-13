from django.shortcuts import render
import math

# Create your views here.
def home(request):
    return render(request,'n_step/n_step.html')

def eval(request):
    S0=float(request.GET["S0"])
    K=float(request.GET["K"])
    r=float(request.GET["r"])
    u=float(request.GET["u"])
    d=float(request.GET["d"])
    T=float(request.GET["T"])
    n=int(request.GET["n"])
    p=((math.pow(math.e,r*(T/n))-d)/(u-d))
    res=0
    for i in range (n+1):
        res=res+((math.pow(p,i))*(math.pow(1-p,n-i)))*(max(S0*math.pow(u,i)*math.pow(d,n-i)-K,0))
    res=res*(math.pow(math.e,(-1)*(r)*(T)))
    return render(request,'n_step/result.html',{'result':res})