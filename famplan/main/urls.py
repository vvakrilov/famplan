from django.urls import path

from famplan.main import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
]
