from pdb import post_mortem
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/login')
def blogs(request):
    if request.method=="POST":
        data=request.POST
        blog_title=request.POST.get('blog_title')
        blog_description=request.POST.get('blog_description')
        blog_image=request.FILES.get('blog_image')
        print(blog_title)
        print('blog_description')
        print('blog_image')

        Blog.objects.create(
            blog_title=blog_title,
            blog_description=blog_description,
            blog_image=blog_image,
        )
        return redirect('/')
    queryset=Blog.objects.all()
    context={'blogs':queryset}
    
    return render(request,'blogs/blogs.html',context)


@login_required(login_url='/login')
def delete_blog(request,id):
    query=Blog.objects.get(id=id)
    query.delete()
    return redirect('/')


@login_required(login_url='/login')
def update_blog(request,id):
    query=Blog.objects.get(id=id)

    if request.method=="POST":
        data=request.POST

        blog_title=request.POST.get('blog_title')
        blog_description=request.POST.get('blog_description')
        blog_image=request.FILES.get('blog_image')

        query.blog_title=blog_title
        query.blog_description=blog_description
        
        if query.blog_image:
            query.blog_image=blog_image

        query.save()
        return redirect('/')

    context={'blog':query}
    return render(request,'blogs/update_blogs.html',context)



def login_page(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login')
        

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login')
        
        else:
            login(request,user)
            return redirect('/')

    return render(request,'blogs/login.html')



def logout_page(request):
    logout(request)
    return redirect('/login')




def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username already taken')
            return redirect('/register')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username         
        )
        user.set_password(password)
        user.save()

        messages.info(request,'account created successfully')
        return redirect('/register')
    return render(request,'blogs/register.html')