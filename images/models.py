from django.db import models


class SimpleModel(models.Model):
    image = models.FileField()
