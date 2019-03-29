# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView,CreateView,View,UpdateView,ListView#,FormView
from django.views.generic import UpdateView
from userr.models import Sign
from django.contrib.auth.forms import UserCreationForm
from management.models import District,Hotel,Place,Gallery,Like,Feedback
from django.contrib.auth.models import User
from management.forms import AddPlace,AddPhoto,AddFeedback,AddHotel,Gallerymenu#,UserForm



# Create your views here.
class HomeView(TemplateView):
	template_name = 'home.html'


# class LoginView(TemplateView):
# 	template_name = 'login.html'


class KasargodView(TemplateView):
	template_name = 'kasargod.html'

class KannurView(TemplateView):
	template_name = 'kannur.html'

class WayanadView(TemplateView):
	template_name = 'wayanad.html'

class KozhikodView(TemplateView):
	template_name = 'kozhikod.html'

class MalapuramView(TemplateView):
	template_name = 'malapuram.html'

class PalakadView(TemplateView):
	template_name = 'palakad.html'


class TrissurView(TemplateView):
	template_name = 'trissur.html'

class ErnakulamView(TemplateView):
	template_name = 'ernakulam.html'

class IdukkiView(TemplateView):
	template_name = 'idukki.html'


class KottyamView(TemplateView):
	template_name = 'kottyam.html'

class AlapuzhaView(TemplateView):
	template_name = 'alapuzha.html'

class PathanamthittaView(TemplateView):
	template_name = 'patanamthitta.html'

class KolllamView(TemplateView):
	template_name = 'kollam.html'

class ThiruvanandapuranmView(TemplateView):
	template_name = 'thiruvanadapuram.html'

class WildLifeiew(TemplateView):
	template_name = 'wildlife.html'

class HikingView(TemplateView):
	template_name = 'hiking.html'

# class HotelView(TemplateView):
# 	template_name = 'index.html'

class BoatView(TemplateView):
	template_name = 'boat.html'

class AyurvedaView(TemplateView):
	template_name = 'ayurveda.html'

class MapView(TemplateView):
	template_name = 'map.html'

class FoodView(TemplateView):
	template_name = 'food.html'


class BookView(TemplateView):
	template_name = 'bh.html'



# class UserView(CreateView):
# 	form_class = User_Form
#  	template_name = 'gallary.html'
#  	success_url = 'success'

class PlaceView(CreateView):
	form_class = AddPlace
 	template_name = 'dict.html'
 	success_url = 'success'

class FeedbackView(CreateView):
	form_class = AddFeedback
 	template_name = 'feedback.html'
 	success_url = 'success'



class AddPhotoForm(CreateView):
	form_class = AddPhoto
	template_name = 'addphoto.html'
	success_url = 'success'

class GallaryView(CreateView):
	form_class = Gallerymenu
 	template_name = 'gallary.html'
 	success_url = 'success'


#class GallaryView(ListView):
	#model = Gallerydata
	#template_name='gupdate.html'	
	#context_object_name = 'gallary_data'


#class ListBookView(ListView):
	#template_name='book.html'	
	#context_object_name = 'Book_data'

		
class ProfilelistView(View):
	template_name = 'user_profile.html'
	def get(self,requst):
		obj = Sign.objects.all()
		context = {
					'profile_list':obj
		}
		return render(requst,self.template_name,context)
		

		




#class BookView(View):
    #template_name = 'addbook.html'
    #form_class = AddBook

    #def get(self,request):
        #return render(request,self.template_name,{'form':form})

    #def post(self,request):
        #form = self.form_class(request.POST)
        #if form.is_valid():
            
            #obj = Book.objects.create(
                #title = request.POST.get('title'),
                #description = request.POST.get('description'),
                #publisher = request.POST.get('publisher'),
                #auther = request.POST.get('auther'),
               #prize = request.POST.get('prize'),
                #time_of_buy = request.POST.get('time_of_buy'))



           # obj.save()

            #return redirect('/music/booklist/')

        #else:
            #form = self.form_class()
            #return render(request,self.template_name,{'form':form})



# 
# class SignUpView(FormView):
# 	template_name = 'registor.html'
# 	form_class = UserForm
# 	model = User

# 	def get(self,request, *args, **kwargs):
# 		self.object = None
# 		form_class = self.get_form_class()
# 		user_form = self.get_form(form_class)
# 		emp_form = UserForm()
# 		return self.render_to_response(self.get_context_data(form1=user_form, form2=emp_form))

# 	def post(self,request,*args,**kwargs):
# 		self.object = None
# 		form_class = self.get_form_class()
# 		user_form = self.get_form(form_class)
# 		emp_form = UserForm(self.request.POST, self.request.FILES)
# 		if (user_form.is_valid() and emp_form.is_valid()):
# 			return self.form_valid(user_form, emp_form)
# 		else:
# 			return self.form_invalid(user_form, emp_form)

# 	def get_success_url(self, **kwargs):
# 		return reverse_lazy('login')

# 	def form_valid(self, user_form, emp_form):
# 		self.object = user_form.save() 
# 		self.object.is_staff=True
# 		self.object.save()
# 		p = emp_form.save(commit=False)
# 		p.user_data = self.object
# 		p.save()
# 		return super(SignUpView, self).form_valid(user_form)
		
# 	def form_invalid(self, user_form, emp_form):
# 		return self.render_to_response(self.get_context_data(form1=user_form,form2=emp_form))

class GallaryUpdate(UpdateView):
	template_name = 'update.html'
	model = Gallery
	success_url = 'management/home/'
	fields = ['user_id','district_id','place_id','feedback_id','image']
			
class HotelUpdate(UpdateView):
	template_name = 'addhotel.html'
	model = Hotel
	success_url = 'management/home/'
	fields = ['hotel_name','address','placet_id','hotel_status']


 # class Loginlist(View):
 # 	template_name = 'login.html'
 # 	def get(self,requst):
 # 		obj = Book.objects.all()
 # 		context = {
 # 					'book_list':obj
 # 		}
 # 		return render(requst,self.template_name,context)