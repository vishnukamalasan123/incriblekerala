from django.conf.urls import url,include
from django.contrib import admin
from userr.models import Sign
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from management.views import HomeView,GallaryView,PlaceView,GallaryUpdate,HotelUpdate,FeedbackView,KasargodView,KannurView,WayanadView,KozhikodView,MalapuramView,PalakadView,TrissurView,ErnakulamView,IdukkiView,KottyamView,AlapuzhaView,PathanamthittaView,KolllamView,ThiruvanandapuranmView,WildLifeiew,HikingView,BoatView,AyurvedaView,FoodView,MapView,BookView,ProfilelistView
urlpatterns = [
    url(r'home/',HomeView.as_view(),name ='home'),
    # url(r'login/',LoginView.as_view(),name ='login'),
    #url(r'^signup/', SignUpView.as_view(), name='signup_page'),
    url(r'gallary/',GallaryView.as_view(),name ='gallary_view'),
    url(r'feedback/',FeedbackView.as_view(),name ='FeedbackView'),
    url(r'kasargod/',KasargodView.as_view(),name ='kasargod'),
    url(r'kannu/',KannurView.as_view(),name ='kannu'),
    url(r'wayanad/',WayanadView.as_view(),name ='wayanad'),
    url(r'kozhikod/',KozhikodView.as_view(),name ='kozhikod'),
    url(r'malapuram/',MalapuramView.as_view(),name ='malapuram'),
    url(r'palakad/',PalakadView.as_view(),name ='palakad'),
    url(r'trissur/',TrissurView.as_view(),name ='trissur'),
    url(r'ernakulam/',ErnakulamView.as_view(),name ='ernakulam'),
    url(r'idukki/',IdukkiView.as_view(),name ='idukki'),
    url(r'kottyam/',KottyamView.as_view(),name ='kottyam'),
    url(r'alapuzha/',AlapuzhaView.as_view(),name ='alapuzha'),
    url(r'pathanamtitta/',PathanamthittaView.as_view(),name ='pathanamtitta'),
    url(r'kollam/',KolllamView.as_view(),name ='kollam'),
    url(r'triruvanandapuram/',ThiruvanandapuranmView.as_view(),name ='triruvanandapuram'),
    url(r'wildlife/',WildLifeiew.as_view(),name ='wildlife'),
    url(r'hiking/',HikingView.as_view(),name ='hiking'),
    url(r'boat/',BoatView.as_view(),name ='boat'),
    # url(r'place/',PlaceView.as_view(),name ='listbook'),
    url(r'ayurveda/',AyurvedaView.as_view(),name ='ayurveda'),
    url(r'food/',FoodView.as_view(),name ='food'),
    url(r'map/',MapView.as_view(),name ='map'),
    url(r'book/',BookView.as_view(),name ='book'),
    url(r'profile/',ProfilelistView.as_view(),name ='profile'),
    url(r'gallary_update/(?P<pk>[0-9]+)/',GallaryUpdate.as_view(),name ='update_gallary'),
    url(r'hotel_update/(?P<pk>[0-9]+)/',HotelUpdate.as_view(),name ='update_hotel'),
    # url(r'login/',Loginlist.as_view(),name ='login'),







    ]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)