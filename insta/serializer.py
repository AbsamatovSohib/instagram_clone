from rest_framework import serializers
from insta import  models


class ProfileSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Profile
        fields = (
            "website_links",
            "name", "gender",
            "bio", "phone",
            "image", "following",
        )


class StoryListSerializer(serializers.ModelSerializer):
    owner_image = serializers.StringRelatedField(source="owner.image")
    owner = serializers.StringRelatedField(source="owner.name")

    class Meta:
        model = models.Story
        fields = (
            "owner", "owner_image", "story_media", "description",
        )


# class

class StorySerializer(serializers.ModelSerializer):
    watched_count = serializers.IntegerField()
    liked_count = serializers.IntegerField()
    story = StoryListSerializer()
    liked_by = serializers.StringRelatedField(many=True)
    watched_by = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Story
        fields = (
            "owner", "owner_image", "story_media", "description","story", "liked_count", "watched_count"
        )


