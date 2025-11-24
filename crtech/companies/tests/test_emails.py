# from django.test import TestCase
# from django.core import mail
# class EmailUnitTest(TestCase):
#     def test_send_email_should_succeed(self)-> None:
#         with self.settings(
#             EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
#         ):  
#             self.assertEqual(len(mail.outbox),0)
#             mail.send_mail(
#             subject="test subject",
#             message="test here",
#             from_email="fb.gerami@gmail.com",
#             recipient_list=["fb.gerami@gmail.com"],fail_silently=False
#             )
#             self.assertEqual(len(mail.outbox),1)
#             self.assertEqual(mail.outbox[0].subject,"test subject")
            
            

from django.test import TestCase
from django.core import mail
import pytest
import json
def test_send_email_should_succeed(mailoutbox,settings)-> None:
        settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
        assert len(mailoutbox)==0
        mail.send_mail(
        subject="test subject",
        message="test here",
        from_email="fb.gerami@gmail.com",
        recipient_list=["fb.gerami@gmail.com"],fail_silently=False
        )
        assert len(mailoutbox)==1
        assert mailoutbox[0].subject=="test subject"          
        
        
from django.urls import reverse
companies_url = reverse("companies:sendmail")
def test_send_email_with_get_verb_should_fail(client)->None:
        response=client.get(companies_url)
        assert response.status_code ==405
        assert json.loads(response.content) == {"detail": "Method \"GET\" not allowed."}
        