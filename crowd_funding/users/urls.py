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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import users
from users.views import *  # ,checkformdata
from users.views import home

urlpatterns = [
    path('loginn', loginPage, name="login"),
    path('reg', UserRegisterView, name='checkdata'),
    path('', home.index, name='home'),
    path('display-category', home.display_category, name='display-category'),
    path('search-for-projects', home.search_for_projects, name='search-for-projects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
