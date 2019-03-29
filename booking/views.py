# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect


# Create your views here.
from django.views.generic import View,ListView,TemplateView
from booking.forms import BookingReg,Hotel_Form,HotelReg,PhotoReg
from booking.models import Hotel1,HotelList,HList,Photo1

from django.contrib.auth.models import User
# from contact.forms import UserForm


class HotelView(View):
    template_name = 'hb.html'
    form_class = BookingReg

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            obj = Hotel1.objects.create(
                # userdata = request.POST.get('userdata'),
                destination = request.POST.get('destination'),
                check_in = request.POST.get('check_in'),
                check_out = request.POST.get('check_out'),
                adults = request.POST.get('adults'),
                children = request.POST.get('children'),
                

)
            obj.save()

            return redirect('home')

        else:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})



class HotelLiatView(ListView):
    template_name='bh.html'	
    context_object_name = 'hotel_data'
    model = HotelList



class BookinglistView(View):
    template_name = 'hotellist.html'
    def get(self,requst):
        obj = HotelList.objects.all()
        context = {
                    'hotel_list':obj
        }
        return render(requst,self.template_name,context)



class HbView(TemplateView):
    template_name = 'hotel1.html'



# class HotelForm(CreateView):
#     form_class = Hotel_Form
#     template_name = 'addhotal.html'
#     success_url = 'success'



class HotelFormView(View):
    template_name = 'addhotal.html'
    form_class = HotelReg

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            
            obj = HList.objects.create(
                # userdata = request.POST.get('userdata'),
                destination = request.POST.get('destination'),
                destination_details= request.POST.get('destination_details'),
                mainfactor = request.POST.get('mainfactor'),
                image = request.FILES.get('image'),
               
                
)
            obj.save()

            return redirect('destinationlist')

        else:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})



class PhotoView(View):
    template_name = 'addphoto.html'
    form_class = PhotoReg

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
        print("get working,",form.errors)
    def post(self,request):

        print("post working")
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            print("if working")
            
            obj = Photo1.objects.create(
                # userdata = request.POST.get('userdata'),
                destination = request.POST.get('destination'),
                mainfactor = request.POST.get('mainfactor'),
                image = request.FILES.get('image'),
               
                
)
            obj.save()

            return redirect('photos')

        else:
            print("else working",form.errors)
            form = self.form_class()
            return render(request,self.template_name,{'form':form})









