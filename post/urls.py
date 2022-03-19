from django.urls import path

from .views import PostView, PostListView

app_name = "post"

urlpatterns = [
    path("", PostView.as_view(), name="create_post"),
    path("feed", PostListView.as_view(), name="feed"),
]
