from django.conf.urls import url, include
from django.contrib import admin
from api import StudentResource
from . import views

student_resource = StudentResource()

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^language/(?P<language>[a-z\-]+)$', views.language, name='language'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid, name='invalid'),
    url(r'^register/$', views.register_student, name='register_student'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^wifi_registration/$', views.wifi_registration, name='wifi_registration'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^search/$', views.search_students, name='search_students'),
    url(r'^api/', include(student_resource.urls)),
]
