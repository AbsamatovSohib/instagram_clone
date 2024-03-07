from django.db import models
from utils.base import BaseModel, GenderTypes
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.db.models import Count


class ProfileManager(models.Manager):
    def is_active(self):
        queryset = self.get_queryset()
        return  queryset.filter(is_public=True)


class Profile(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="profile_owner")
    website_links = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=255)

    gender = models.CharField(choices=GenderTypes.choices, default=GenderTypes.MALE, max_length=30)
    bio = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, null=True, blank=True)

    image = models.ImageField(upload_to="img/user/", null=True, blank=True, validators=[FileExtensionValidator(
        allowed_extensions=[".jpeg", ".img", "png"]
    )])

    is_public = models.BooleanField(default=True)
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True,)


    def __str__(self):
        return self.name


class Media(BaseModel):
    image = models.FileField(upload_to="post/", null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=[
            "IMG", "SVG", "PNG", "JPEG", "wbem", "avi", "mp4"])
    ])


class StoryStatisticManager(models.Manager):
    def get_active(self):
        queryset = self.get_queryset()
        return queryset.filter(
            created_at__lte=timezone.now()-timezone.timedelta(hours=24))

    def count_watched(self):
        queryset = self.get_queryset()
        return queryset.annotate(user_count=Count('watched_by'))

    def count_likes(self):
        queryset = self.get_queryset()
        return queryset.annotate(user_count=Count('liked_by'))


class Story(BaseModel):
    owner = models.ForeignKey(Profile, related_name="story_owner", on_delete=models.CASCADE)
    story_media = models.ManyToManyField(Media, related_name="story_post",  blank=True)
    description = models.CharField(max_length=256)

    watched_by = models.ManyToManyField(Profile, related_name="story_watched_user")
    liked_by = models.ManyToManyField(Profile, related_name="story_liked_by")

    # owner_info = models.JSONField()

    story_active = StoryStatisticManager

    # def save(self):
    #     owner_info = {"owner":self.owner.name,
    #                   "image":self.owner.image,
    #                   }
    #     super.save()
# def json_created_signal(sender, instance, created, **kwargs):
#         instance.owner_info = {
#         "owner_name": instance.owner.name,
#         "image": instance.owner.image,
#         }
#         instance.owner_info.save()
# post_save.connect(json_created_signal, sender=Story)


class StoryHighlight(BaseModel):
    name = models.CharField(max_length=127)
    stories = models.ManyToManyField(Story, related_name="highlighted_stories")


class Region(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class District(BaseModel):

    region = models.ForeignKey(Region, related_name="region", on_delete=models.CASCADE, )
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(BaseModel):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="owner")
    content = models.ManyToManyField(Media, related_name="post_medias")
    description = models.TextField(null=True, blank=True)

    liked_by = models.ManyToManyField(Profile, related_name="liked_post_by", blank=True)
    watched_by = models.ManyToManyField(Profile, related_name="watched_post_by", blank=True)
    saved_by = models.ManyToManyField(Profile, related_name="watched_saved_by", blank=True)

    def __str__(self):
        return self.description[:30]


class Comments(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    description = models.TextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comment_owner")

    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="comment_reply", null=True, blank=True)

    def __str__(self):
        return self.description[:30]
