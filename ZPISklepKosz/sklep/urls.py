
from django.urls import path
from . import views
from .views import PasswordsChangeView, PasswordsResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('home/', views.index, name="home"),
    path('oNas/', views.oNas),
    path('kontakt/', views.kontakt),
    path('regulamin/', views.regulamin),
    path('platnosc/', views.platnosc),
    path('zwroty/', views.zwroty),
    path('newsletter/', views.newsletter),
    path('logowanie/', views.logowanie),
    path('rejestracja/', views.rejestracja),
    path('wylogowanie/', views.wylogowanie),
    path('zmianaHasla/', PasswordsChangeView.as_view(template_name='zmiana.html')),
    path('zmianaHaslaSuccess/', views.password_success, name="password_success"),
    path('konto/', views.konto),
    path('model/', views.model),
    path('usunKonto/', views.usunKonto),
    path('zapisbrak/', views.zapisbrak),
    path('aplikacja/', views.aplikacja),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='reset_password'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),name='password_reset_sent'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_conf.html'),name='password_reset_conf'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_compl.html'),name='password_reset_compl'),
]

