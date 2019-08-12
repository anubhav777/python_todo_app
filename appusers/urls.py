from django.urls import path
from .views import user_form,login_view,logout_view

app_name="appusers"

urlpatterns=[
      path('register/',user_form),
      path('login/',login_view),
      path('logout/',logout_view,name='logoutview')
]