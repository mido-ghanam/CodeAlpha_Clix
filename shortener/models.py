from django.db import models
import uuid

class ShortURL(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
  full_url = models.URLField()
  short_code = models.CharField(max_length=10, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
