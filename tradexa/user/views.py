from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import SignUpForm
from .forms import SignUpForm,PostForm
from django.contrib import messages,auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully')
            fm.save()
            return HttpResponseRedirect('login')

    else:
            fm=SignUpForm()
    return render (request,'sign_up.html',{'form':fm})

def login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            
            if fm.is_valid():
                uname=fm.cleaned_data['username']
            
                upass=fm.cleaned_data['password']
                
                user=authenticate(username=uname,password=upass)
                
                if user is not None:
                    auth.login(request,user)
                    
                    return HttpResponseRedirect("post")
        else:
                fm=AuthenticationForm( )        


        return render (request,'login.html',{'form':fm}) 
    else:
        return HttpResponseRedirect('post') 


def post_up(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
               form.save(request)
               messages.success(request, "New post added.")
               return HttpResponseRedirect('product')

        else:            
            form = PostForm()
    else:
        return HttpResponseRedirect('login')          
      
    return render(request,'post.html',{'form':form}) 
     

def user_logout(request):
    logout(request)    
    return HttpResponseRedirect('login')