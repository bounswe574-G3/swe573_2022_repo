from django.db import models
from django.contrib.auth.models import User


class AnnotationModel(models.Model):
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    annotation = models.JSONField()
    uri = models.CharField(max_length=4096, blank=True)
    annotation_id =models.CharField(max_length=200)
    def __str__(self):
        return str(self.annotation)