import json

from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
import math
from django.db.models import Avg, Count, Q, Sum
from comments.models import Comments
from comments.forms import CommentForm
from .models import Projects, Images, Donation, Rating, Tags
from django.forms import modelformset_factory
from projects.forms import ProjectForm,  DonationForm
from .models.projects import Category
from users.models import User
from comments.forms import ReportCommentForm
from .forms import ReportProjectForm
from .models.reported_project import ReportedProject, Report
from .models.rating import Rate
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    query = request.GET.get('q')
    if query and query  != "@":
        # convert the query from string separated with space  to array
        query = query.split(",")
        query = [q.lower() for q in query]
        all_projects = Projects.objects.filter(Q(tags__tag_name__in=query) | Q(title__in=query)).order_by("-id").distinct()
    else:
        all_projects = Projects.objects.all()

    paginator = Paginator(all_projects,4)  # 4 project per page
    page = request.GET.get("page")
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    context = {
        'projects': projects,
    }
    return render(request, 'projects/index.html', context)



def createProject(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectForm(request.POST)

            if form.is_valid():
                project_form = form.save(commit=False)
                project_form.save()
                form.save_m2m()

                for _img in request.FILES.getlist('project_images[]'):
                    FileSystemStorage(location='/images')
                    photo = Images(
                                project=project_form, path=_img)
                    photo.save()

                for tag in request.POST["project_tags"].split(","):
                    Tags(project=project_form, tag_name=tag).save()

                # user profile page
                return redirect("project_details", project_form.id)

        else:

            project_form = ProjectForm(

                initial={"user": request.user})

            return render(request, 'projects/create_project.html/',
                          {'project_form': project_form})
    else:
        return redirect('login')


def projectDonate(request, id):
    if request.user.is_authenticated:
        project = Projects.objects.get(id=id)
        if request.method == 'POST':
            form = DonationForm(request.POST)
            if form.is_valid():
                result = Donation.objects.filter(
                    Q(project_id=id) & Q(user_id=request.POST['user'])).count()
                print(result)
                if (result > 0):
                    obj = Donation.objects.filter(Q(project_id=id) & Q(
                        user_id=request.POST['user'])).first()
                    amount_value = getattr(obj, 'amount')
                    Donation.objects.filter(Q(project_id=id) & Q(user_id=request.POST['user'])).update(
                        amount=amount_value + int(request.POST['amount']))
                else:
                    donate_form = form.save(commit=False)
                    donate_form.save()

                print(result)
                return redirect("project_details", project.id)

        else:
            donate_form = DonationForm(
                initial={"project": id, "user": request.session['_auth_user_id']})
            return render(request, 'projects/donate_project.html/', {'donate_form': donate_form, "project": project})
    else:
        return redirect('login')




def project_details(request, id):
    if request.user.is_authenticated:
        add_rate = 0
        project = Projects.objects.get(id=id)
        comments = Comments.objects.filter(project=project)
        project_category = Category.objects.get(id=project.category_id)
        user = User.objects.get(id=request.user.pk)

        projectimage = project.images_set.first()
        if projectimage != None:
            projectimage = projectimage.path.url
            picturesObjects = project.images_set.all()
            pictures = []
            for picture in picturesObjects:
                pictures.append(picture.path.url)

        # Checking on Donations
        total_target = project.total_target * 0.25
        amount = 0
        donations = Donation.objects.filter(project_id=id)
        for donation in donations:
            amount = amount + donation.amount

        # check if user rated the project
        try:
            rate = Rate.objects.get(project=project, user=user)
            is_rated = True
            rating = rate.rate
        except Rate.DoesNotExist:
            is_rated = False
            rating = 0

        # get the average rating for the project
        try:
            project.rating
        except Rating.DoesNotExist:
            Rating.objects.create(project=project)

        average_rating = project.rating.get_average_rating()

        # check if user reported this project
        try:
            report = Report.objects.get(project=project, user=request.user)
            is_reported = True
        except Report.DoesNotExist:
            is_reported = False

        if request.method == "GET":
            comment_form = CommentForm()
            report_comment_form = ReportCommentForm()
            report_project_form = ReportProjectForm()
            context = {
                "project": project,
                "pictures": pictures,
                "total_target": total_target,
                "amount": amount,
                "comments": comments,
                "project_category": project_category,
                "is_rated": is_rated,
                "is_reported": is_reported,
                "rating": rating,
                "average_rating": average_rating,
                "comment_form": comment_form,
                "report_comment_form": report_comment_form,
                "report_project_form": report_project_form,
                "user_id": user.id,
            }
            return render(request, 'projects/project_page.html/', context)
        else:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.project = project
                new_comment.user = User.objects.get(id=request.user.pk)
                # Save the comment to the database
                new_comment.save()
            else:
                comment_form = CommentForm()
            # report_comment_form = ReportCommentForm()
            context = {
                "project": project,
                "pictures": pictures,
                "total_target": total_target,
                "amount": amount,
                "comments": comments,
                "project_category": project_category,
                "is_rated": is_rated,
                "rating": rating,
                "average_rating": average_rating,
                "comment_form": comment_form,
                "user_id": user.id,
                # "report_comment_form": report_comment_form,
            }
        return redirect("project_details", project.id)
    else:
        return redirect('login')



def report_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == 'POST':
        report_message = request.POST.get('report')

        response_data = {}
        Report.objects.create(project=project, user=request.user, report_message=report_message)

        try:
            project.reportedproject
        except ReportedProject.DoesNotExist:
            ReportedProject.objects.create(project=project)

        project.reportedproject.incrementOne()
        project.reportedproject.save()
        response_data['result'] = "report successful"
        response_data['project_id'] = project.id

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse("Reported")


def rate_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        user = User.objects.get(id=request.POST.get('user'))

        response_data = {}
        Rate.objects.create(project=project, user=user, rate=rating)

        try:
            project.rating
        except Rating.DoesNotExist:
            Rating.objects.create(project=project)

        if rating == '1':
            project.rating.one_star += 1
        elif rating == '2':
            project.rating.two_star += 1
        elif rating == '3':
            project.rating.three_star += 1
        elif rating == '4':
            project.rating.four_star += 1
        elif rating == '5':
            project.rating.five_star += 1

        project.rating.save()
        response_data['result'] = "rating successful"
        response_data['average_rating'] = project.rating.get_average_rating()

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse("Rated")
