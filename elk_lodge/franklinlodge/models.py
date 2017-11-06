from django.db import models

# Create your models here.
class Elk_Member(models.Model):
	elk_member_type = models.CharField(max_length=50)
	elk_first_name = models.CharField(max_length=20)
	elk_last_name = models.CharField(max_length=50)
	elk_member_email_address = models.CharField(max_length=100)
	elk_member_nickname = models.CharField(max_length=30)
	elk_member_since_date = models.DateTimeField('date joined')

class Elk_Photos(models.Model):
	elk_member = models.ForeignKey(Elk_Member, on_delete=models.CASCADE)
	photo_type = models.CharField(max_length=100)
	photo_url = models.CharField(max_length=100)
	photo_description = models.CharField(max_length=300)

class Dues(models.Model):
	due_type = models.CharField(max_length=100)
	due_amount = models.IntegerField(default=0)

class Events(models.Model):
	event_type = models.CharField(max_length=100)
	event_date = models.DateTimeField('date of event')

class Elk_NewsLetter(models.Model):
	new_subscriber = models.CharField(max_length=1)
	subscriber_first_name = models.CharField(max_length=20)
	subscriber_last_name = models.CharField(max_length=50)
	subscriber_email_address = models.CharField(max_length=100)
	newsletter_title = models.CharField(max_length=200)
	archive_urls = models.CharField(max_length=100)
	archive_date = models.DateTimeField('elk newsletter date')

class Elk_Contact(models.Model):
	contact_first_name = models.CharField(max_length=20)
	contact_last_name = models.CharField(max_length=50)
	contact_email_address = models.CharField(max_length=100)
	inquiry_title = models.CharField(max_length=250)
	inquiry_content = models.CharField(max_length=500)

class Membership_Application(models.Model):
	prospective_member_first_name = models.CharField(max_length=20)
	prospective_member_last_name = models.CharField(max_length=50)
	prospective_member_email_address = models.CharField(max_length=100)
	prospective_member_address = models.CharField(max_length=300)
	prospective_membership_type = models.CharField(max_length=100)