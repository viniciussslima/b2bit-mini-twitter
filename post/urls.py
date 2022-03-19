from django.urls import path

from .views import PostView, PostListView

urlpatterns = [
    path("", PostView.as_view()),
    path("feed", PostListView.as_view()),
]
