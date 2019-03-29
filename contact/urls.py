from django.conf.urls import url

from contact.views import ContactsView


urlpatterns = [
       url(r'contacts/',ContactsView.as_view(),name='contacts'),
      # url(r'update/',(?<pk>[0-9]+),student_,name='form'),
       

]
