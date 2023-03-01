from django.db import models


# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=512)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
