from django.conf.urls import url

from booking.views import HotelView,HotelLiatView,BookinglistView,HbView,HotelFormView,PhotoView


urlpatterns = [
       url(r'hotal/',HotelView.as_view(),name='hotal'),
       url(r'hotal_list/',HotelLiatView.as_view(),name='hotal_list'),
       url(r'booking_list/',BookinglistView.as_view(),name='booking_list'),
       url(r'hb/',HbView.as_view(),name='hb'),
       url(r'hform/',HotelFormView.as_view(),name='hform'),
       url(r'photo/',PhotoView.as_view(),name='photo'),
      # url(r'update/',(?<pk>[0-9]+),student_,name='form'),
       

]
