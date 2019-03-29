# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect


# Create your views here.
from django.views.generic import View
from userr.forms import SignReg
from userr.models import Sign
from django.contrib.auth.models import User
from userr.forms import UserForm


class SignCreateView(View):
    template_name = 'registor.html'
    form_class = UserForm
    #usr_cnt = SignReg

    def get(self,request):
        form1 = self.form_class()
        form2 = SignReg()
        return render(request,self.template_name,{'form1':form1,'form2':form2})

    def post(self,request):
        form1 = self.form_class(request.POST,request.FILES)
        form2 = SignReg(request.POST,request.FILES)
        print("in posttttttttttttttttt")
        if form1.is_valid() and form2.is_valid():
            print("in valid")
            usr = User.objects.create_user(
                username = request.POST.get('username'),
            	first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                password = request.POST.get('password1'))
                # password1 = request.POST.get('password2'))

            usr.is_staff=True
            usr.save()
            emp = Sign.objects.create(
                userdata = usr,
                dob = request.POST.get('dob'),
                address = request.POST.get('address'),
                ph_no = request.POST.get('ph_no'),
                image = request.FILES.get('image'))


            emp.save()

            return redirect('/admin2/login')

        else:
            print("in else")
            form1 = self.form_class()
            form2 = SignReg()
            return render(request,self.template_name,{'form1':form1,'form2':form2})
