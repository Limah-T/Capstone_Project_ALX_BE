from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),

    # login view
    path('login', views.LoginView.as_view(), name='login_view'),

    # corporate and individual form views
    path('individualmemberform', views.IndividualView.as_view(), name='individual_view'),
    path('cooperatememberform', views.CooperateView.as_view(), name='cooperate_view'),

    # list views
    path('individual_database_view', views.IndividualDataBaseView.as_view(), name='ind_view'),
    path('coperate_database_view', views.CorporateDatabaseView.as_view(), name='cop_view'),
    path('staff_database_view', views.StaffDatabaseView.as_view(), name='staff_view'),
    path('director_database_view', views.DirectorDatabaseView.as_view(), name='director_view'),

    # detail views
    path('individual_detail_view/<int:pk>', views.IndividualDetailView.as_view(), name='ind_detail'),
    path('coporate_detail_view/<int:pk>', views.CorporateDetailView.as_view(), name='cop_detail'),
    path('staff_detail_view/<int:pk>', views.StaffDetailView.as_view(), name='staff_detail'),
    path('director_detail_view/<int:pk>', views.DirectorDetailView.as_view(), name='director_view'),

    # logout view
    path('logout', views.logoutview, name='logout_view'),
]

