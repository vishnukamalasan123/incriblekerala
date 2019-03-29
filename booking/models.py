from __future__ import unicode_literals

from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Photo1(models.Model):
	#userdata= models.OneToOneField(User)
	destination = models.CharField(max_length = 100)
	Destination_details = models.CharField(max_length = 100)
	mainfactor = models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'media/images')
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.destination
class Hotel1(models.Model):
	#userdata= models.OneToOneField(User)
	destination = models.CharField(max_length = 100)
	check_in = models.DateField(auto_now = True)
	check_out = models.DateField(auto_now = True)
	adults = models.IntegerField()
	children = models.IntegerField()
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.destination


class HotelList(models.Model):
	# userdata= models.OneToOneField(User)
	destination = models.CharField(max_length = 100)
	check_in = models.DateField(auto_now = True)
	check_out = models.DateField(auto_now = True)
	adults = models.IntegerField()
	children = models.IntegerField()
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.destination


class HList(models.Model):
	#userdata= models.OneToOneField(User)
	destination = models.CharField(max_length = 100)
	destination_details = models.CharField(max_length=200)
	mainfactor = models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'media/images')
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.destination










