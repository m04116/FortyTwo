from django.test import TestCase
from django.core.urlresolvers import reverse

from user_info.models import UserInformation


class AboutmeTest(TestCase):

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

    def test_view_uses_correct_template(self):
            resp = self.client.get(reverse('info'))
            self.assertEqual(resp.status_code, 200)
            self.assertTemplateUsed(resp, 'user_info/user_data.html')