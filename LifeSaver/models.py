from django.db import models
from .utils import get_input_image_path, get_output_image_path
import uuid as UUID
# Create your models here.


class Lungs(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=UUID.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    input_image = models.FileField(
        upload_to=get_input_image_path, null=True, blank=True)
    output_image = models.FileField(
        upload_to=get_output_image_path, null=True, blank=True)
    verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
