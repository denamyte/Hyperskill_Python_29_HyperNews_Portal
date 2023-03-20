from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming),
    path('news/', views.MainView.as_view()),
    path('news/<int:link>/', views.ArticleView.as_view()),
]
