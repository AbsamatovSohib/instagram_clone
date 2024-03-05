from django.db import models
from utils.base import BaseModel, GenderTypes
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator


class Profile(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="profile_owner")
    website_links = models.CharField(max_length=256, null=True, blank=True)

    gender = models.CharField(choices=GenderTypes.choices, default=GenderTypes.MALE, max_length=30)
    bio = models.CharField(max_length=150)

    is_public = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.user.id


class Images(BaseModel):
    image = models.ImageField(upload_to="post/", null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=["IMG, SVG, PNG, JPEG, GIF"])
    ])


class Post(BaseModel):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="owner")
    description = models.TextField(null=True, blank=True)

    image = models.ManyToManyField(Images, related_name="images_for_post")
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    # comment = models.(Profile, through="Comments",  blank=True, null=True, )
    # liked_by = models.ManyToManyField(Profile, through="Liked_post")
    # saved_by = models.ManyToManyField(Profile, through="Saved_post")

    def __str__(self):
        return self.description[:30]


class Comments(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    description = models.TextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comment_owner")

    def __str__(self):
        return self.description[:30]


class LikedPost(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_posts")
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="liked_owner")


class SavedPost(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="saved_posts")
    saved_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="saved_by_owner")


class Followers(BaseModel):
    followed_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followed_by")
    followed_to = models.ManyToManyField(Profile, related_name="followed_to")


class Following(BaseModel):
    followed_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following_by")
    followed_to = models.ManyToManyField(Profile, related_name="following_to")


class Story(BaseModel):
    owner = models.ForeignKey(Profile, related_name="story_owner")
    post_as_story = models.ForeignKey(Post, related_name="story_post", null=True, blank=True)

    is_active = models.BooleanField(default=True)
    mention = models.ManyToManyField(Profile, related_name="mentioned")

    description = models.CharField(max_length=256)
