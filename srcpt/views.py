from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from srcpt.models import Contact
from srcpt.models import Mssg
from srcpt.models import add_Blog
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,"home.html")

def About(request):
    return render(request,"about.html")


def Contact(request):
     if request.method == "POST": 
        n = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        # print(name, email, phone, subject, desc)
        cont=Contact(name=n, email=email, phone=phone, subject=subject,
                          desc=desc, date=datetime.today())
        cont.save()
        messages.success(request, 'Your Message has been sent!')
     return render(request, 'contact.html')


def Blog(request):
   
    return render(request,"blog.html")


def Add_Blog(request):
    if request.method == 'POST':
        tit = request.POST.get('tit')
        category = request.POST.get('category')
        content = request.POST.get('content')
        summary = request.POST.get('summary')
        image = request.POST.get('image')

        blog=Add_Blog(tit=tit,category=category,content=content,summary=summary,image=image,date=datetime.today())
        blog.save()

    return render(request, "add_blog.html")




def Mssg(request):

    if request.method == 'POST':
        n = request.POST.get('name')
        m = request.POST.get('mobile')
        ps = request.POST.get('purpose')

        sms=Mssg(name=n, mobile=m,purpose=ps)
        sms.save()
        messages.success(request, 'Your Message has been sent!')
      

    return render(request, "mssg.html")


def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
            messages.success(request, 'Your Message has been sent!')
    return render(request, 'signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        user = authenticate(request, username=username, password1=pass1)

        return redirect('home')
        messages.success(request, 'Your Message has been sent!')
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('login')
