from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('songs/', views.SongsList.as_view()),
    path('snippets/<int:pk>/', views.SongsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)