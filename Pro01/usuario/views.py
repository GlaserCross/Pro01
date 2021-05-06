from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.forms import ModelForm
from django.urls import reverse_lazy


from .forms import RegisterForm

# Create your views here.

#def index(request):
    #return render(request,
        #'register.html',
        #)




def register(request):
    if request.method == 'POST':
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Cuenta creada satisfactoriamente!')
            return redirect('index')

    else:
        f = RegisterForm()

    return render(request, 'register.html', {'form': f})

