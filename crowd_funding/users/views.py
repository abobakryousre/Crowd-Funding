from django.db.models import Sum
from django.http import JsonResponse, Http404
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from projects.models import Donation, Images, Projects

from .forms import UserProfile
from .models import User
from django.contrib import messages

# from projects.models.projects import Donation

# Create your views here.
def index(request):
    return render(request, 'users/index.html')


def edit_profile(request):
    if request.method == "GET":
        # will replace static user_id with the current_user id like -> request.user.pk
        user_id = User.objects.first().pk
        current_user = User.objects.get(pk=user_id)
        user_profile = UserProfile(instance=current_user)
        # is there any checks here ?
        context = {"user_profile": user_profile}
        return render(request, "users/edit_profile.html", context)
    else:
        user_id = User.objects.first().pk
        current_user = User.objects.get(pk=user_id)
        updated_data = UserProfile(request.POST, request.FILES, instance=current_user)
        if updated_data.is_valid():
            updated_data.save()
            return redirect('index')
        else:
            context = {"user_profile": updated_data}
            return render(request, "users/edit_profile.html", context)


def view_profile(request):
    # get user information
    current_user = User.objects.first()  # will change with request.usr.pk
    projects_of_specific_user = Projects.objects.filter(user_id = 1)
    donations=Donation.objects.select_related('project').filter(user_id=1)

    context = {"current_user": current_user,
    "projects":projects_of_specific_user,
    "donations":donations
    }

    return render(request, 'users/profile.html', context)


def check_password(request):
    if request.is_ajax():
        password = request.GET.get("password");
        user = User.objects.first()
        if user.password == password:
            return JsonResponse({"isPasswordCorrect": True})
        else:
            return JsonResponse({"isPasswordCorrect": False})
    else:
        return HttpResponse("Page Not Found!");


def delete_account(request):
    return redirect('index')

def change_password(request):
    if request.method == "GET":
        return render(request, 'users/change_password.html')
    else:
        #User.objects.get(pk=request.user.pk)
        current_user = User.objects.first()
        user_password = current_user.password
        if user_password == request.POST.get("old-password"):
            if request.POST.get('password1') == request.POST.get('password2'):
                current_user.password = request.POST.get("password1")
                current_user.save()
                return redirect('profile')
            else:
                context = {'error': "New Passwords Not match"}
                return render(request, 'users/change_password.html', context)
        else:
            context = {'error': "Old Passwords Incorrect"}
            return render(request, 'users/change_password.html', context)

def deleteItem(request,pk):


    project = Projects.objects.get(id=pk)
    try:
        sum_donations_of_project = Donation.objects.values('project_id').order_by('project_id').annotate(
            total_price=Sum('amount')).get(project_id=pk)
        if sum_donations_of_project["total_price"] >= project.total_target * (25 / 100):
            return redirect('user-projects')

    except Donation.DoesNotExist:
        project.delete()
        return redirect('user-projects')


# return HttpResponse(str(project.total_target))
   #  if sum_donations_of_project.exists():
   #      if sum_donations_of_project["total_price"] >= project.total_target * (25 / 100):
   #          return redirect('user-projects')
   #      else:
   #          project.delete()
   #          return redirect('user-projects')
   #
   #  else:
   #      project.delete()
   #      return redirect('user-projects')






def show_user_projects(request):
    projects_of_specific_user = Projects.objects.filter(user_id=1)

    context = {
               "projects": projects_of_specific_user,

               }

    return render(request, 'users/projects_of_user.html', context)











