from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    data = CounterData.objects.all()
    if request.method =="POST":
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CountryDataForm()
    context={'data':data, 'form':form}
    return render(request,'dashboard/index.html',context)

