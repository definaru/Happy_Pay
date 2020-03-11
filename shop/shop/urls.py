from django.contrib import admin
from django.urls import re_path, path
from store import views
from django.views.defaults import server_error, page_not_found, permission_denied

# app_name = 'store'

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^contact', views.contact, name='contact'),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^signup', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    re_path(r'^403$', views.handler403),
    re_path(r'^404$', views.handler404),
    re_path(r'^500$', views.handler500),
];