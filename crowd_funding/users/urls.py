"""crowd_funding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import authentication as auth
from .views import (change_password, check_password, delete_account,
                    deleteItem, edit_profile, home, index, show_user_donations,
                    show_user_projects, view_profile)

urlpatterns = [
    path('loginn', auth.loginPage, name="login"),
    path('reg', auth.UserRegisterView, name='checkdata'),
    path('display-category', home.display_category, name='display-category'),
    path('search-for-projects', home.search_for_projects, name='search-for-projects'),
    path("profile/edit", edit_profile, name="edit-profile"),
    path("profile/", view_profile, name="profile"),
    path('profile/check-password', check_password, name="check-password"),
    path('delete-account/', delete_account, name='delete-account'),
    path('profile/change-password', change_password, name='change-password'),
    url(r'^deleteItem/(?P<pk>\d+)$', deleteItem,name='deleteItem'),
    path('profile/my-projects', show_user_projects, name="user-projects"),
    path('profile/my-donations', show_user_donations, name="user-donations"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
