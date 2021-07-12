from django.shortcuts import render,HttpResponseRedirect
from .forms import ProductForm
from django.contrib import messages,auth
# Create your views here.


def productview(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
               form.save(request)
               messages.success(request, "New post added.")
               return HttpResponseRedirect('product')

        else:            
            form = ProductForm()
    else:
        return HttpResponseRedirect('login')          
      
    return render(request,'product.html',{'form':form}) 