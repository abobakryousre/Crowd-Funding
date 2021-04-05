from django.shortcuts import render, redirect
# from users.form import Usermodelform
from django.contrib.auth import login, authenticate, logout
from users.forms import createuserform
from users.forms import loginformauth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registerpage(request):
    # render form
    if request.method == 'GET':
        form = createuserform()
        context = {
            'formregister': form
        }
        return render(request, 'users/form.html', context)

        # check on data
        # is valied => save data on database
        # not => render form again
    else:
        fulldata = createuserform(request.POST, request.FILES)

        if fulldata.is_valid():
            fulldata.save()
            # email=fulldata.cleaned_data('email')
            # raw_password=fulldata.cleaned_data('password1')
            # users=authenticate(email=email,passwor=raw_password)
            # login(request,users)
            return render(request,'users/home.html')
        else:
            context = {"formregister": fulldata}
            return render(request, 'users/form.html', context)


def loginform(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return render(request, 'users/home.html')
    if request.POST:
        form = loginformauth(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, passwor=password)
            if user:
                login(request, user)
                return render(request, 'users/home.html')
    else:
        form = loginformauth()
        context = {
            'formlogin': form
        }
        return render(request,'users/login.html', context)

    # if user is uath
    # => render login form
    # check if email,password =>

# def checkformdata(request):
#     fulldata=createuserform(request.POST)
#
#     if fulldata.is_valid():
#         fulldata.save()
#         return render(request,'users/login.html')
#     else:
#         context={"formregister":fulldata}
#         return render(request,'users/form.html',context)


# def create(requset):
#     form=Usermodelform(requset.POST)
#     form.save()
# return redirect("/users")
