from django.db import models
from django.contrib.auth.models import User

class UserProfiles(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    twitter_link = models.CharField(max_length=255, default="", blank=True)
    github_link = models.CharField(max_length=255, default="", blank=True)
    description_text = models.TextField(default="", blank=True)
