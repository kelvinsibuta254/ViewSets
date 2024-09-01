from django.db import models

# Create your models here.
class Member(models.Model):
    name  = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=5, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)