from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class GenderTypes(models.TextChoices):
    MALE = "MALE",
    FEMALE = "FEMALE",
    CUSTOM = "CUSTOM",
    NOTMENTION = "NOTMENTION",



