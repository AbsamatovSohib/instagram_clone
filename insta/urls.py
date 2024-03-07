from django.urls import path
from insta import views

urlpatterns = [
    path("profile/list/", views.ProfileListView.as_view()),
    path("profile/<int:pk>", views.ProfileDetailView.as_view()),

    path("story/", views.StoryListView.as_view()),
    path("story/<int:pk>")
]
