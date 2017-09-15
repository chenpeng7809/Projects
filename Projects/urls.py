"""Projects URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from MyApp.views import index, category, add_category, add_page, register, user_login, restricted, user_logout, about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category'),
    url(r'^add_category/', add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', add_page, name='add_page'),
    url(r'^register/', register, name='register'),
    url(r'^login/', user_login, name='user_login'),
    url(r'^restricted/', restricted, name='restricted'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^about/$', about, name='about'),

]
