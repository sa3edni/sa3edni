from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('signin',views.signin),
    path('signup', views.signup),
    path('profile', views.profile),
    path('calculator', views.calculator),
    path("signout", views.signout),
    path("selectuni", views.uniSelection),
    path("mselection", views.majorselection),
    path("download", views.download),
    path("about", views.about),
    path("unis", views.unis),
    path("unimore",views.uniMore),
    path("readmore",views.newsMore),
    path("resetpass", views.resetPassword),
    path("resetpass", views.resetPassword)
]

