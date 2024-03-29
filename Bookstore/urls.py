"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# config/urls.py
from allauth.account.views import logout
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include # new




urlpatterns = [

    # Django admin
    path('admin/', admin.site.urls),

    # User management
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

    # path('logout', logout, name='logout'),
    # url(r'^signup/$', core_views.signup, name='signup'),

    # Local apps
    # path('accounts/', include('accounts.urls')), # new
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]
