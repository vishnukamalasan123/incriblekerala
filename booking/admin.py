# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from booking.models import Hotel1,HotelList,HList,Photo1

admin.site.register(Hotel1)
admin.site.register(HotelList)
admin.site.register(HList)
admin.site.register(Photo1)