# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect


# Create your views here.
from django.views.generic import View
from contact.forms import ContactsReg
from contact.models import Contacts
from django.contrib.auth.models import User
# from contact.forms import UserForm


class ContactsView(View):
    template_name = 'contact.html'
    form_class = ContactsReg

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            obj = Contacts.objects.create(
                full_name = request.POST.get('full_name'),
                email = request.POST.get('email'),
                message_1 = request.POST.get('message_1')

)
            obj.save()

            return redirect('home')

        else:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})
