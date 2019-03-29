from __future__ import unicode_literals

from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Sign(models.Model):
	userdata= models.OneToOneField(User)
	dob = models.DateField()
	address = models.CharField(max_length = 200)
	ph_no = models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'media/photos')
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.userdata.username