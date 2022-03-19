from django.urls import path

from famplan.main import views as view

urlpatterns = (
    path('', view.TemporaryView.as_view(), name='temporary test page'),
)