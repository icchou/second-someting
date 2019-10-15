from django.db import models
from django.utils import timezone

# Create your models here.
class Datafile(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/',max_length=100, blank=True, null=True)
    iteration = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
