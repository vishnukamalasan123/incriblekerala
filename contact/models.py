from __future__ import unicode_literals

from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Contacts(models.Model):
	# userdata= models.OneToOneField(User)
	full_name = models.CharField(max_length = 100)
	email = models.EmailField()
	message_1 = models.TextField(max_length = 100)
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.full_name