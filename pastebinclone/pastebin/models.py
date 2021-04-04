import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Pastebin(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000, help_text='Enter your paste here...')
    pub_date = models.DateTimeField('date published', null=True)
    syntax = models.CharField(max_length=15, null=True)
   
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('pastebin-detail', args=[str(self.id)])

    def __str__(self):
        return self.syntax

    class Meta:
        ordering = ['pub_date']

