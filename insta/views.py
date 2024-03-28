# from insta import serializer, models
# from rest_framework import generics
# from django.db.models import Count
# from django.db.models.functions import Coalesce
#
#
# class ProfileListView(generics.ListAPIView):
#     queryset = models.Profile.objects.all().filter(is_public=True)
#     serializer_class = serializer.ProfileSerializer
#
#
# class ProfileDetailView(generics.RetrieveAPIView):
#     queryset = models.Profile.objects.all().filter(is_public=True)
#     serializer_class = serializer.ProfileSerializer


# class StoryListView(generics.ListAPIView):
#     queryset = models.Story.story_active.get_active.select_related(
#         'owner', "owner.name", "owner.image")
#     serializer_class = serializer.StoryListSerializer

    # def get_queryset(self):
    #     return super().get_queryset().filter(owner=request.user)


# class StoryDetailView(generics.RetrieveAPIView):
#     queryset = models.Story.story_active.get_active.all()
#     serializer_class = serializer.StorySerializer

    # def get_queryset(self, request):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(owner=request.user).annotate(Coalesce(
    #         watched_count=Count("watched_by"),
    #         liked_count=Count("liked_by"),
    #     ), 0)
    #
    #     return queryset

from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<html><title>To-Do lists</title></html>")
