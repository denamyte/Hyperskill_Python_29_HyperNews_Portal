from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming),
    path('news/<int:link>/', views.ArticleView.as_view())
]
