from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.signup),
    path('signup_data/',views.signup_data),
    path('login/',views.login),
    path('login_data/',views.login_data),
    path('table/',views.table),
    path('update/<int:uid>/',views.update),
    path('update_data/',views.update_data),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete")
]
