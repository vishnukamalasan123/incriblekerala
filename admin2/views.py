from __future__ import unicode_literals
from contact.models import Contacts
from userr.models import Sign
from booking.models import HList,Photo1
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View,UpdateView
# from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm
# from management.models import District,Hotel,Place,Gallery,Like,Feedback
from django.contrib.auth.models import User
from userr.forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.core.exceptions import ObjectDoesNotExist
from booking.forms import HotelReg



class AdminView(TemplateView):
	template_name = 'admin_hom.html'
	

class MassagelistView(View):
    template_name = 'mesage_list.html'
    def get(self,request):
        obj = Contacts.objects.all()
        context = {
                    'message_list':obj
        }
        return render(request,self.template_name,context)

class DestinationlistView(View):
    template_name = 'destination_list.html'
    def get(self,request):
        obj = HList.objects.all()
        context = {
                    'destination_list':obj
        }
        return render(request,self.template_name,context)
        
class Destination1listView(View):
    template_name = 'destination_list1.html'
    def get(self,request):
        obj = HList.objects.all()
        context = {
                    'destination_list1':obj
        }
        return render(request,self.template_name,context)
        success_url = '/admin2/destination1list'

class UserlistView(View):
    template_name = 'user_list.html'
    def get(self,request):
        obj = Sign.objects.all()
        context = {
                    'user_list':obj
        }
        return render(request,self.template_name,context)


class PhotolistView(View):
    template_name = 'photo_list.html'
    def get(self,request):
        obj = Photo1.objects.all()
        context = {
                    'photo_list':obj
        }
        return render(request,self.template_name,context)

  
class LoginView(View):
    template_name='login.html'

    def get(self,request):
        form = UserForm
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            if user.is_staff == True and user.is_superuser == False:
                print("inside fn")
                return redirect('home')
            if user.is_superuser == True and user.is_staff == True:
                print("inside else")
                return redirect('admin1')
        else:
            return redirect('login')


class DestinationUpdateView(UpdateView):
    template_name = 'updated.html'
    model = HList
    success_url = '/admin2/destination1list'
    fields = ['destination','destination_details','mainfactor','image']





# class DestinationUpdateView(View):
#     template_name='update.html'

#     def get(self,request):
#         form = HList
#         return render(request,self.template_name,{'form':form})
#     def post(self,request):
#         destination = request.POST['destination']
#         destination_details = request.POST['destination_details']
#         mainfactor = request.POST['mainfactor']
#         image = request.POST['image']
        
#         user = authenticate(request,destination = destination,estination_details  = estination_details ,mainfactor=mainfactor,image=image)
#         if user is not None:
#             login(request,user)
#             if user.is_staff == True and user.is_superuser == False:
#                 print("inside fn")
#                 return redirect('home')
#             if user.is_superuser == True and user.is_staff == True:
#                 print("inside else")
#                 return redirect('admin1')
#         else:
#             return redirect('login')
