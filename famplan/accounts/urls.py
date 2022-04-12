from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views


urlpatterns = (
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('register/', views.UserRegisterView.as_view(), name='register'),

    path('<int:pk>/', views.ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', views.ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),

    path('profile/edit/', views.EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/', views.DeleteProfileView.as_view(), name='delete profile'),
)

