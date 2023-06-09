"""firstproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp.views import hello, hello1, hello2, students
from students.views import listone, listall, post, postform, delete, edit
                                       #別名
from CookieSessionApp import views as csviews

from flower import views as fviews
from django.conf import settings
from django.conf.urls.static import static

from news import views as nviews
from boardapp import views as bviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('hello1/<str:username>/', hello1),
    path('hello2/<str:username>/', hello2),
    path('std/', students),
    path('listone/', listone),
    path('listall/', listall),
    path('post/', post),
    path('postform/', postform),
    path('delete/<str:stdID>/', delete),
    path('edit/<str:stdID>/', edit),
    path('edit/<str:stdID>/<str:mode>/', edit),
    #cookies
    path('set_cookie/<str:key>/<str:value>/', csviews.set_cookie),
    path('set_cookie2/<str:key>/<str:value>/', csviews.set_cookie2),
    path('get_cookie/<str:key>/', csviews.get_cookie),
    path('get_allcookies/', csviews.get_allcookies),
    path('delete_cookie/<str:key>/', csviews.delete_cookie),
    path('pagecount/', csviews.pagecount),
    # sessions
    path('set_session/<str:key>/<str:value>/', csviews.set_session),
    path('get_session/<str:key>/', csviews.get_session),
    path('get_allsessions/', csviews.get_allsessions),
    # vote
    path('vote/', csviews.vote),	
    path('set_session2/<str:key>/<str:value>/', csviews.set_session2),
    path('delete_session/<str:key>/', csviews.delete_session),
    # login
    path('login/', csviews.login),	
    path('logout/', csviews.logout),

    path('mypage/', csviews.mypage),
    path('adduser/', csviews.adduser),
    path('register/', csviews.register),

    # news
    path('newsindex/', nviews.newsindex),
	path('newsindex/<str:pageindex>/', nviews.newsindex),
	path('newsdetail/<int:detailid>/', nviews.newsdetail),
	path('newslogin/', nviews.newslogin),
	path('newslogout/', nviews.newslogout),
	path('newsadminmain/', nviews.newsadminmain),
	path('newsadminmain/<str:pageindex>/', nviews.newsadminmain),
 	path('newsadd/', nviews.newsadd),
	path('newsedit/<int:newsid>/', nviews.newsedit),
	path('newsedit/<int:newsid>/<str:edittype>/', nviews.newsedit),
	path('newsdelete/<int:newsid>/', nviews.newsdelete),
	path('newsdelete/<int:newsid>/<str:deletetype>/', nviews.newsdelete),

    # post
    path('showpost/', bviews.showpost),
    path('addpost/', bviews.addpost),
    path('captcha/', include('captcha.urls')),

    # allauth
    path('accounts/', include('allauth.urls')),
    path('captcha/', include('captcha.urls')),

    path('flower/', fviews.flowers),
    path('flower/create/', fviews.create, name='create'),
    path('flower/edit/<int:pk>/', fviews.edit, name='edit'),
    path('flower/delete/<int:pk>/', fviews.delete, name='delete'),
    path('flower/<slug:slug>/', fviews.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

