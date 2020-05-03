#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#			INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

from django.urls import include, re_path
from django.contrib import admin
from taskManager import taskManager_urls
from taskManager import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^taskManager/', include(taskManager_urls, namespace="taskManager")),
    re_path(r'^admin/', admin.site.urls, name='adminsites'),
]




