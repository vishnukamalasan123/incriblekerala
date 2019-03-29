# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Create your models here.
# class UserContinuation(models.Model):
#     #user_id = models.OneToOneField(User)
#     First_Name = models.CharField(max_length=20)
#     Last_Name = models.CharField(max_length=12)
#     #email = models.EmailField()
#     username = models.CharField(max_length=200)
#     password1 = models.CharField(max_length=200)
#     password2 = models.CharField(max_length=200)
#     created_on = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.First_Name


class District(models.Model):
	district_id = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	image = models.ImageField(upload_to = 'media/images')
    #publisher = models.CharField(max_length=100)
	#district_direction = models.CharField(max_length=100)
	

	def __str__(self):
		return self.district_id


class Hotel(models.Model):

    hotel_name = models.OneToOneField(User)	
    address = models.TextField(max_length=200)
    placet_id = models.IntegerField()
    image = models.ImageField(upload_to ='media/images')
    hotel_status = models.DateField()
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.user_data.hotel_name



class Place(models.Model):
    place_id = models.OneToOneField(User)	
    district_id = models.TextField(max_length=200)
    place_number = models.IntegerField()
    place_name = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.place_name
class Feedback(models.Model):
    user_id = models.OneToOneField(User)   
    district_id = models.TextField(max_length=200)
    place_id = models.IntegerField()
    feedback_id = models.IntegerField()
    feedback_by = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.feedback_by


class Gallery(models.Model):
    user_id = models.OneToOneField(User)   
    district_id = models.TextField(max_length=200)
    place_id = models.IntegerField()
    feedback_id = models.IntegerField()
    image = models.ImageField(upload_to ='media/images')
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.studebt_data

class Like(models.Model):
    user_id = models.OneToOneField(User)   
    district_id = models.TextField(max_length=200)
    place_id = models.IntegerField()
    like_status = models.TextField(max_length=200)
    liked_by = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.user_id

class Login(models.Model):
    Login = models.OneToOneField(User)  
    First_Name = models.TextField(max_length=200)
    Last_Name = models.TextField(max_length=200)
    username = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    password = models.IntegerField()
    password2 = models.IntegerField()
    #Login = models.ImageField(upload_to ='media/files')
    #dob = models.DateField()
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.username

# class SignUp(models.Model):
#     # First_Name = models.TextField(max_length=200)
#     # Last_Name = models.TextField(max_length=200)
#     # #username = models.TextField(max_length=200)
#     # email = models.TextField(max_length=200)
#     # password = models.IntegerField()
#     # password2 = models.IntegerField()
#     # #user_id = models.OneToOneField(User)   
#     #username = models.TextField(max_length=200)
#     #image = models.ImageField(upload_to ='media/images')
#     #email = models.TextField(max_length=200)
#     created_on = models.DateTimeField(auto_now=True)