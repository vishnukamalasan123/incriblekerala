from django.conf.urls import url
from contact.models import Contacts
from booking.models import Photo1
from userr.models import Sign
from booking.forms import HotelReg

from admin2.views import AdminView,MassagelistView,LoginView,PhotolistView,UserlistView,DestinationUpdateView,Destination1listView,DestinationlistView


urlpatterns = [
       url(r'admin/',AdminView.as_view(),name='admin1'),
      # url(r'update/',(?<pk>[0-9]+),student_,name='form'),
       url(r'messagelist/',MassagelistView.as_view(),name='messagelist'),
       url(r'destinationlist/',DestinationlistView.as_view(),name='destinationlist'),
       url(r'destination1list/',Destination1listView.as_view(),name='destination1list'),
       url(r'photos/',PhotolistView.as_view(),name='photos'),
       url(r'user_list/',UserlistView.as_view(),name='user_list'),
       url(r'^update/(?P<pk>[0-9]+)/',DestinationUpdateView.as_view(),name='update'),
       url(r'login/',LoginView.as_view(),name='login'),
       

]
