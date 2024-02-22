from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    status = models.BooleanField(default=False,blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class NoteHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    change = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.change