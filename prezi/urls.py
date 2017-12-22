from django.conf.urls import url
from prezi import views

urlpatterns = [
    url(r'^$', views.prezi_list, name='prezi_list'),
]
