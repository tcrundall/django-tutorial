"""playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.views.generic import RedirectView

import accounts.views as accounts_views
import boards.views as boards_views

urlpatterns = [
    re_path('^$', boards_views.home, name='home'),
    re_path('^signup/$', accounts_views.signup, name='signup'),
    re_path('^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path('^boards/(?P<pk>\d+)/$', boards_views.board_topics, name='board_topics'),
    re_path('^boards/(?P<pk>\d+)/new/$', boards_views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
    # re_path('^(?P<username>[\w.@+-]+)/$', boards_views.user, name='user'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
