from django.shortcuts import render , redirect
# from users.form import Usermodelform
from django.contrib.auth import login ,authenticate
from users.forms import createuserform
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerpage(request):

    # render form
    if request.method == 'GET':
        form = createuserform()
        context={
            'formregister':form
        }
        return render(request,'users/form.html',context)

        # check on data
        # is valied => save data on database
        # not => render form again
    else:
        fulldata = createuserform(request.POST)

        if fulldata.is_valid():
            fulldata.save()
            return render(request, 'users/login.html')
        else:
            context = {"formregister": fulldata}
            return render(request, 'users/form.html', context)


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