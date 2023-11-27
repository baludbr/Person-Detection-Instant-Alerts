
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.MyClass.as_view()),
]
