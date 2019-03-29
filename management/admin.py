from __future__ import unicode_literals

from django.contrib import admin
from management.models import District,Place,Feedback,Gallery,Like,Hotel#,SignUp

#from book.models import Book

# Register your models here.
admin.site.register(District)
admin.site.register(Place)
# admin.site.register(UserContinuation)
admin.site.register(Feedback)
admin.site.register(Gallery)
admin.site.register(Like)
admin.site.register(Hotel)
#admin.site.register(SignUp)


