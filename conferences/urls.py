from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<zosia_id>\d+)/register$', views.register, name='user_zosia_register'),
]