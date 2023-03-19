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
    # PASSWORD RESETTING
    re_path(
        '^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt',
        ),
        name='password_reset',
    ),
    re_path(
        '^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done',
    ),
    re_path(
        '^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    re_path(
        '^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete',
    ),

    # PASSWORD SETTING
    re_path(
        '^settings/password/$',
        auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change',
    ),
    re_path(
        '^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done',
    ),

    # HOME
    re_path('^$', boards_views.home, name='home'),

    # USER
    re_path('^signup/$', accounts_views.signup, name='signup'),
    re_path('^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path('^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # BOARDS
    re_path('^boards/(?P<pk>\d+)/$', boards_views.board_topics, name='board_topics'),
    re_path('^boards/(?P<pk>\d+)/new/$', boards_views.new_topic, name='new_topic'),
    re_path(
        '^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$',
        boards_views.topic_posts,
        name='topic_posts',
    ),
    re_path(
        '^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$',
        boards_views.reply_topic,
        name='reply_topic',
    ),

    # ADMIN
    path('admin/', admin.site.urls),
    # re_path('^(?P<username>[\w.@+-]+)/$', boards_views.user, name='user'),

    # CONFIGURATION
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]

