from django.conf.urls import url
from . import views

app_name='LoginPage'
urlpatterns=[
    url(r'^$', views.choice, name='choice'),
    url(r'^login/$', views.loginform, name='loginform'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^submit/',views.add_model, name='add_model'),
    url(r'^profile/',views.find_model, name='find_model'),
    url(r'^profile-photo/',views.upload, name='upload'),
    url(r'^upload/',views.uploadvideo,name='uploadvideo'),
    url(r'^logout/',views.logout1,name='logout'),
    url(r'^profile-videos/',views.usermainview,name='usermainview'),
]
