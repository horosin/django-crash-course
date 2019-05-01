from django.db import models
from django.contrib.auth.models import User


class SampleType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Sample(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    type = models.ForeignKey(SampleType, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
