from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.LoginView.as_view(), name='login_view'),
    path('individualmemberform', views.IndividualView.as_view(), name='individual_view'),
    path('cooperatememberform', views.CooperateView.as_view(), name='cooperate_view'),
    path('check_ind/<int:pk>', views.check_ind, name='check_ind'),
    path('logout', views.logoutview, name='logout_view'),
]

