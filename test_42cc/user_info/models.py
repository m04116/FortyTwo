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
