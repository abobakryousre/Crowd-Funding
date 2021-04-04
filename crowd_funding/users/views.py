from django.shortcuts import render
from projects.models import Projects, Rating
# Create your views here.
def index(request):
    # TODO: slider, for highest 5 reated projects
    # get the highest 5 rate
    highest_rate = Rating.objects.all().order_by('-five_star')[:5]
    highest_rated_projects = []
    for rate in highest_rate:
        highest_rated_projects.append(rate.project)
    # TODO: five-latest-projects
    latest_five_projects = Projects.objects.all().order_by('-created_at')[:5]
    # TODO: list of 5 projects selected by admin
    # TODO: each category and display  it's projects with ajax request
    # TODO: search bar, with projects tag, and title.
    context = {
        'highest_projects': highest_rated_projects,
        'latest_projects': latest_five_projects
    }
    return render(request, 'users/index.html', context)