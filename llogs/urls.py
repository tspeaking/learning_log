from django.conf.urls import url

from . import views

app_name = 'llogs'
urlpatterns = [
    url(r'^$', views.index, name='index')
]