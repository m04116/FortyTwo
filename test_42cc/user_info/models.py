from datetime import date, datetime
from django.db import models
# from sorl.thumbnail import ImageField, get_thumbnail

class UserInformation(models.Model):
    name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True, default=None)
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50,)
    other_contacts = models.TextField(blank=True, null=True, default=None)
    photo = models.ImageField(upload_to='user_photo/', blank=True, null=True)
    # photo = models.ImageField(upload_to='user_photo/', blank=True, null=True,
                              # height_field='height_field', width_field='width_field')
    # height_field = models.IntegerField(default=200)
    # width_field = models.IntegerField(default=200)

    # def save(self, *args, **kwargs):
    #     if self.photo:
    #         self.photo = get_thumbnail(self.photo, '200x000', quality=100, format='JPEG')
    #     super(UserInformation, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name


class Request(models.Model):
    request_date = models.DateField(default=date.today)
    scheme = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    method = models.CharField(max_length=250)
    content_type = models.CharField(max_length=250)
    is_viewed = models.BooleanField(default=False)