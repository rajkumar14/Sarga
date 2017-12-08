"""Learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_view,name='home_view'),
    url(r'^home/$',index_view,name='index_view'),
    url(r'^contact-us/$',contact_us,name='contact_us'),
    url(r'^about-us/$',about_us,name='about_us'),
    url(r'^services/$',services,name='services'),
    url(r'^portfolio/$',portfolio,name='portfolio'),
    url(r'^blog/$',blog,name='blog'),
    url(r'^career/$',career,name='career'),
    url(r'^faq/$',faq,name='faq'),
    url(r'^terms/$',terms,name='terms'),
    url(r'^privacy/$',privacy,name='privacy'),
    url(r'^registration/$',registration,name='registration'),
    url(r'^typography/$',typography,name='typography'),
    url(r'^company-location/$',company_location,name='company_location'),
    url(r'^company-coordinate/$',company_coordinate,name='company_coordinate'),####hospital-coordinate
]

