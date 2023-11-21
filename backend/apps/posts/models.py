from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import SoftDeletableModel, TimeStampedModel
from datetime import datetime
from django.urls import reverse
from django_resized import ResizedImageField

from apps.authentication.managers import UserManager

# Create your models here.

class Post(TimeStampedModel, SoftDeletableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=112, blank=True, null=True, default=0)
    prepopulated_fields = {"slug": ("title",)}
    image =  ResizedImageField(size=[250, 200], upload_to='images')
    video = models.FileField(upload_to='videos/',blank=True, null=True, default=0)


    user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,  # You can adjust the on_delete behavior based on your requirements
    related_name='posts',  # Optionally, set a related name for reverse lookups
    )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={'slug': self.slug})
