from django.test import TestCase

from user_info.models import UserInformation


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # UserInformation.objects.get(id=1)
        UserInformation.objects.create(
            name = 'Konstantin',
            last_name = 'Rodin',
            date_of_birth = '1980-03-23',
            bio = "From my youth I wanted to code. Now I'm starting...",
            email = 'krodinv@gmail.com',
            jabber = 'krodinv@42cc.co',
            skype = 'inbox011',
            other_contacts = '+380632435463')

    def test_name_label(self):
        user = UserInformation.objects.get(id=1)
        field_label = UserInformation._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_name_max_length(self):
        user = UserInformation.objects.get(id=1)
        max_length = UserInformation._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
