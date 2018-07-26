from django.urls import path
from . import views

urlpatterns = [
    path('api/iaeee/', views.LeadListCreate.as_view()),
]
