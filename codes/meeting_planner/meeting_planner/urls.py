"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
# import welcome function from views in website app
from website.views import welcome, date, about
from meetings.views import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # the first argument specifies the url 
    # and the second argument is the actual view functionb
    #path('welcome.html', welcome),

    # make welcome.html show as the index (default) page
    path('', welcome),
    path('date', date),
    path('about', about),
    path('meetings/<int:id>', detail),

]


