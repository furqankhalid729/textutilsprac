from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('remove_pun',views.remove_pun,name='remove_pun')
]