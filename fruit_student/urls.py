from django.urls import path
from . import views
urlpatterns=[
    path('',views.fruit_student,name='fruit_student')
]