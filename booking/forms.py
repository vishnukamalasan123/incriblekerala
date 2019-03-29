from django import forms
from booking.models import Hotel1,HotelList,HList,Photo1

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['first_name','last_name','email','username','password1','password2']




class BookingReg(forms.ModelForm):
	class Meta:
		model = Hotel1
		exclude = ('created_on','userdata',)


class HotelReg(forms.ModelForm):
	class Meta:
		model = HList
		exclude = ('created_on','userdata',)



class Hotel_Form(forms.ModelForm):
	class Meta:
		model =HotelList

		exclude = ('created_on','userdata',)

class PhotoReg(forms.ModelForm):
	class Meta:
		model = Photo1
		exclude = ('created_on','userdata',)



