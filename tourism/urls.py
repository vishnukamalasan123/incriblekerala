"""testprojt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from management import views
# from userr import views
from django.contrib.auth import views as auth_View
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^management/',include('management.urls')),
    url(r'^userr/',include('userr.urls')),
    # url(r'^login/',auth_View.login,{"template_name" :"login.html"}, name = 'login'),
    url(r'^logout/',auth_View.logout,{'next_page':settings.LOGOUT_REDIRECT_URL}, name = 'logout'),
    url(r'^contact/',include('contact.urls')),
    url(r'^booking/',include('booking.urls')),
    url(r'^admin2/',include('admin2.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)