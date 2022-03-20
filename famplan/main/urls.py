from django.urls import path

from famplan.main import views as view

urlpatterns = (
    path('', view.HomePage.as_view(), name='temporary test page'),
)