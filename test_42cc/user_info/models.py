from datetime import date, datetime
from django.db import models

class UserInformation(models.Model):
    name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True, default=None)
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50,)
    other_contacts = models.TextField(blank=True, null=True, default=None)


class Request(models.Model):
    request_date = models.DateField(default=date.today)
    scheme = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    method = models.CharField(max_length=250)
    content_type = models.CharField(max_length=250)
    is_viewed = models.BooleanField(default=False)