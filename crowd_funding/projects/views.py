from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
import math
from django.db.models import Avg, Count, Q, Sum

from comments.models import Comments
from .models import Projects, Images, Donation ,Rating,Tags

from django.forms import modelformset_factory
from projects.forms import ProjectForm, PictureForm, DonationForm
from .models.projects import Category


def createProject(request):
    ImageFormSet = modelformset_factory(
        Images, form=PictureForm, extra=3)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid:
            project_form = form.save(commit=False)
            project_form.save()
            # field = project_form.cleaned_data['tags']
            # tags =  request.POST['tags'].split(',')
            form.save_m2m()

            for pictureForm in formset.cleaned_data:
                if pictureForm:
                    image = pictureForm['path']
                    photo = Images(
                        project=project_form, path=image)
                    photo.save()

            for tag in request.POST["project_tags"].split(","):
                Tags(project=project_form, tag_name=tag).save()

            # user profile page
            return redirect("projects_index")
            # return HttpResponse("project added and redirect to user profile")
    else:
        picture_form = ImageFormSet(queryset=Images.objects.none())
        project_form = ProjectForm(

            initial={"user":  request.session['_auth_user_id']})

        return render(request, 'projects/create_project.html/',
                      {'project_form': project_form, 'picture_form': picture_form})


def projectDonate(request, id):
    project = Projects.objects.get(id=id)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            result = Donation.objects.filter(
                Q(project_id=id) & Q(user_id=request.POST['user'])).count()
            print(result)
            if (result > 0):
                print("hjhjhj")
                obj = Donation.objects.filter(Q(project_id=id) & Q(
                    user_id=request.POST['user'])).first()
                amount_value = getattr(obj, 'amount')
                Donation.objects.filter(Q(project_id=id) & Q(user_id=request.POST['user'])).update(
                    amount=amount_value + int(request.POST['amount']))
            else:
                donate_form = form.save(commit=False)
                donate_form.save()

            print(result)
            return redirect("projects_index")
            # return HttpResponse("donations has been added and redirect to
            # user profile")
    else:
        donate_form = DonationForm(
            initial={"project": id, "user": request.session['_auth_user_id']})
        return render(request, 'projects/donate_project.html/', {'donate_form': donate_form, "project": project})

def index(request):
    return render(request, 'projects/donate_project.html/')



def project_details(request, id):
    add_rate = 0
    project = Projects.objects.get(id=id)
    project_category = Category.objects.get(id=project.category_id)

    # projectimage = project.path.first()
    # if projectimage != None:
    #     projectimage = projectimage.picture.url
    #     picturesObjects = project.projectpictures_set.all()
    #     pictures = []
    #     for picture in picturesObjects:
    #         pictures.append(picture.picture.url)


    # Checking on Donations
    total_target = project.total_target * 0.25
    amount = 0
    donations = Donation.objects.filter(project_id=id)
    for donation in donations:
        amount = amount + donation.amount

    # Getting All Comments
    comments = Comments.objects.filter(project_id=id)

    context = {
        "project": project,


        "total_target": total_target,
        "amount": amount,
        "comments": comments,
        "project_category":project_category

    }
    return render(request, 'projects/project_page.html/', context)
