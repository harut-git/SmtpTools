"""tryTen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from profiles import views as profiles_views
from contact import views as contact_views
from generate import views as generate_views
from smtp_send import views as smtp_views
from demo import views as dynamic_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^products/$', generate_views.products, name='products'),
    url(r'^generate/$', generate_views.generate_form, name='generate_form'),
    url(r'^send/$', smtp_views.sender_form, name='sender_form'),
    url(r'^dms/$', dynamic_views.dms, name='dms'),
    url(r'^zero/$', generate_views.home, name='zero_home'),
    url(r'^cabinets/$', dynamic_views.cabinets, name='cabinets'),
    url(r'^finalize/$', dynamic_views.finalize, name='finalize'),
    url(r'^accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
