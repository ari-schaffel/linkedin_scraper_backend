from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('backend/', views.SnippetList.as_view()),
    path('backend/<int:pk>/', views.SnippetDetail.as_view()),
    path('backend/urls', views.UrlList.as_view()),
    path('simple/', views.SimpleList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)