import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Elk_Member(models.Model):
	elk_member_type = models.CharField(max_length=50)
	elk_first_name = models.CharField(max_length=20)
	elk_last_name = models.CharField(max_length=50)
	elk_member_email_address = models.CharField(max_length=100)
	elk_member_nickname = models.CharField(max_length=30)
	elk_member_since_date = models.DateTimeField('date joined')

	def __str__(self):
		return self.elk_member_type

	def __str__(self):
		return self.elk_first_name
	
	def __str__(self):
		return self.elk_last_name
	
	def __str__(self):
		return self.elk_member_email_address
	
	def __str__(self):
		return self.elk_member_nickname

	def __str__(self):
		return str(self.elk_member_since_date)

	def was_added_recently(self):
		return self.elk_member_since_date >= timezone.now() - datetime.timedelta(days=1)

class Elk_Photos(models.Model):
	elk_member = models.ForeignKey(Elk_Member, on_delete=models.CASCADE)
	photo_type = models.CharField(max_length=100)
	photo_url = models.CharField(max_length=100)
	photo_description = models.CharField(max_length=300)

	def __str__(self):
		return self.elk_member
	
	def __str__(self):
		return self.photo_type
	
	def __str__(self):
		return self.photo_url
	
	def __str__(self):
		return self.photo_description

class Dues(models.Model):
	due_type = models.CharField(max_length=100)
	due_amount = models.IntegerField(default=0)

	def __str__(self):
		return self.due_type
	
	def __str__(self):
		return self.due_amount


class Events(models.Model):
	event_type = models.CharField(max_length=100)
	event_date = models.DateTimeField('date of event')

	def __str__(self):
		return self.event_type

	def __str__(self):
		return self.event_date


class Elk_NewsLetter(models.Model):
	new_subscriber = models.CharField(max_length=1)
	subscriber_first_name = models.CharField(max_length=20)
	subscriber_last_name = models.CharField(max_length=50)
	subscriber_email_address = models.CharField(max_length=100)
	newsletter_title = models.CharField(max_length=200)
	archive_urls = models.CharField(max_length=100)
	archive_date = models.DateTimeField('elk newsletter date')


	def __str__(self):
		return self.new_subscriber

	def __str__(self):
		return self.subscriber_first_name
	
	def __str__(self):
		return self.subscriber_last_name

	def __str__(self):
		return self.subscriber_email_address

	def __str__(self):
		return self.newsletter_title

	def __str__(self):
		return self.archive_urls

	def __str__(self):
		return self.archive_date

class Elk_Contact(models.Model):
	contact_first_name = models.CharField(max_length=20)
	contact_last_name = models.CharField(max_length=50)
	contact_email_address = models.CharField(max_length=100)
	inquiry_title = models.CharField(max_length=250)
	inquiry_content = models.CharField(max_length=500)

	def __str__(self):
		return self.contact_first_name

	def __str__(self):
		return self.contact_last_name

	def __str__(self):
		return self.contact_email_address

	def __str__(self):
		return self.inquiry_title

	def __str__(self):
		return self.inquiry_content


class Membership_Application(models.Model):
	prospective_member_first_name = models.CharField(max_length=20)
	prospective_member_last_name = models.CharField(max_length=50)
	prospective_member_email_address = models.CharField(max_length=100)
	prospective_member_address = models.CharField(max_length=300)
	prospective_membership_type = models.CharField(max_length=100)

	def __str__(self):
		return self.prospective_member_first_name

	def __str__(self):
		return self.prospective_member_last_name

	def __str__(self):
		return self.prospective_member_email_address
	
	def __str__(self):
		return self.prospective_member_address

	def __str__(self):
		return self.prospective_membership_type
