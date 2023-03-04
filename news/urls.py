from django.urls import path
from .views import NewsView, NewDetailView

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('news/<int:pk>/', NewDetailView.as_view(), name='new-detail'),

]
