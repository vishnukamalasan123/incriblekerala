from django import forms

from management.models import Hotel,Gallery,Feedback,Hotel,Place#,SignUp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class User_Form(forms.ModelForm):
# 	class Meta:
# 		model = UserContinuation
# 		exclude = ('created_on','First_Name')
		
class AddHotel(forms.ModelForm):
	class Meta:
		model = Hotel
		exclude = ('created_on',)

class AddPlace(forms.ModelForm):
	class Meta:
		model = Place
		exclude = ('created_on',)

class AddFeedback(forms.ModelForm):
	class Meta:
		model = Feedback
		exclude = ('created_on',)

class AddPhoto(forms.ModelForm):
	class Meta:
		model = Gallery
		exclude = ('created_on',)

class Gallerymenu(forms.ModelForm):
	class Meta:
		model = Gallery
		exclude = ('created_on',)

class Gallerydata(forms.ModelForm):
	class Meta:
		model = Gallery
		exclude = ('created_on',)

# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		exclude = ('created_on','userdata',)


#class Gallerymenu(forms.ModelForm):
	##model = Gallery
		#exclude = ('created_on',)		


# class UserForm(UserCreationForm):

# 	# def __init__(self,*args,**kwargs):
# 	# 	super(UserForm,self).__init__(*args,**kwargs)
# 	# 	self.fields['username'].required = True
# 	# 	self.fields['email'].required = True
# 	# 	self.fields['first_name'].required = True
# 	# 	self.fields['password1'].required = True
# 	# 	self.fields['password2'].required = True

# 	class Meta:
# 		model = User
# 		fields = ('first_name','last_name','email','username','password1','password2')