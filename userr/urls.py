from django.conf.urls import url

from userr.views import SignCreateView


urlpatterns = [
       url(r'signup/',SignCreateView.as_view(),name='signup'),
      # url(r'update/',(?<pk>[0-9]+),student_,name='form'),
       

]
